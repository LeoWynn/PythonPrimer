import os
import sys
import time
import socket
import zipfile
from subprocess import Popen, PIPE, STDOUT

#---------------------------------------# 
#            DATA STRUCTS               #
#---------------------------------------#

##
#  script_info -> GLOBAL: for script environment related data
##

script = {'prefix'         :       'Unknown',
	  'folder'         :       'Unknown',
	  'log'            :            None}

##
#  target_info -> GLOBAL: for target related data
##

target = {'astris'         :            None,
	  'astris_host'    :     'localhost',
	  'astris_probe'   :       'Unknown',
	  'astris_vers'    :       'Unknown',
	  'astris_probefw' :       'Unknown',
	  's3e_auto-gate'  :		False}

##
#  factory_info -> global: for factory related data
##

factory = {'factory_build'         :       'unknown',
	   'factory_bundle'        :       'unknown',
	   'factory_test'          :       'unknown',
	   'factory_config'        :       'Unknown',
	   'factory_serialno'      :       'Unknown',
	   'factory_host'          :       'Unknown'}

##
#  panic_info -> GLOBAL: for panic related data
##

panic = {'failure'	:	'Unknown',
	 'state'	:	'Unknwon',
	 'panic_str'	:	'Unknown',
	 'stackshot'	:	    False,
	 'soc'		:	'Unknown',
	 'soc_rev'	:	'Unknown',
	 'cpu_reg'	:	'Unknown',
	 'cpu_states'	:	'Unknwon'}

##
#   coproc -> GLOBAL: for co-processor related data
##

coproc = {'ans'         :       False,
          'sio'         :       False,
	  'gfx'		:	False,
          'sdio'        :       False,
	  'aop'		:	False,
	  'spu'		:	False,
	  'aop_rt'	:	False}

##
#   s3e_list-> GLOBAL: for SoCs with s3e
##

s3e_list = ['Maui', 'Malta', 'Elba' , 'Cayman', 'Myst']


#---------------------------------------#
#               RANDOM                  #
#---------------------------------------#

##
#  progress_bar() - Prints a progress indication based on 'cmd'
##

def progress_bar(cmd, output):

        # kernel coredump status
        if ('coredump' in cmd):
                if ('time_remaining' in output):
                        print output.split(' ')[0] + '\b'*6,

#---------------------------------------#
#               STDIO                   #
#---------------------------------------#

##
#  proc_read() - Read lines from stdout synchronously
##

def proc_read(proc, cmd):

        # Check if script log setup
        if (script['log'] != None):

                # Write CMD to log 
                script['log'].write('CMD: ' + cmd + '\n')

        # Create empty list
        output_list = list()

        while True:
                # Wait for end of stdout or astris prompt
                output = proc.stdout.readline()     #function, read info
                if (not output) or (output == 'astris>\n'):
                        #print '[No more data]'
                        break
                #print output

                # Check if script log setup
                if (script['log'] != None):

                        # Write raw output to script log
                        script['log'].write(output)

                # Strip '\n' and '\t' from returned line
                output_stripped = output.strip('\n\t')
        
                # Update progress bar
                if ('coredump' in cmd):
                        progress_bar(cmd, output_stripped)

                # Build list of stripped returned lines
                output_list.append(output_stripped)

        return output_list

##
#  proc_spawn() - Spawn process
##

def proc_spawn(cmd):

        # Spawn provided process
        proc = Popen(cmd, stdin = PIPE, stdout = PIPE, stderr = STDOUT, bufsize = 0, universal_newlines = True, shell = False)

        # Convert CMD array into string
        cmd = ' '.join(cmd)

        # Retrieve list of read lines
        ret = proc_read(proc, cmd)
        
        return ret, proc

##
#  proc_write() - Write command into stdin
##

def proc_write(proc, cmd):

        # Convert CMD array into string
        cmd = ' '.join(cmd)

        # Write provided command to stdin
        proc.stdin.write(cmd + '\n')

        # Retrieve list of read lines
        ret = proc_read(proc, cmd)
        
        return ret


#---------------------------------------#
#              DEVICE INFO              #
#---------------------------------------#

##
#  factory_probe() - Ask user to specify probe
##

def factory_probe():

        # Spawn 'astrisctl list' process
        cmd = ['astrisctl', 'list']
        read_val = proc_spawn(cmd)[0]

        # Check if no probes
        if (len(read_val) == 1):

                # Print error and quit
                print "No Probes Connected"
                sys.exit()

        # Parse returned values
        for probe in read_val[1:]:

                # Print available probes
                print read_val.index(probe),'\b)', probe

        # Ask user which probe
        sel = raw_input("Select probe or 'q': ")

        # Check if user wants to quit
        if (sel == 'q'):
                sys.exit()

        # Convert response to integer
	try:
		sel_num = int(sel)
        # Check if non valid entry
	except ValueError:
                # Print error and quit
                print "Invalid Response"
                sys.exit()

	# Check if non valid entry
	if (sel_num  > (len(read_val)-1)) or (sel_num <= 0):

		# Print error and quit
		print "Invalid Response"
		sys.exit()
	

        # Write 'astris_probe' to target_info
        target['astris_probe'] = read_val[sel_num]


##
#  factory_details() -> Asks user for factory related info
##

def factory_details():

        # Ask user for build
        factory['factory_build'] = raw_input("HW Build: ").upper()

        # Ask user for bundle
        factory['factory_bundle'] = raw_input("SW Bundle: ")

        # Ask user for test
        factory['factory_test'] = raw_input("Test: ")

        # Ask user for config
        factory['factory_config'] = raw_input("Config: ").upper()

        # Ask user for serial no.
        factory['factory_serialno'] = raw_input("Serial No: ").upper()

	# Require serial no.
	if (factory['factory_serialno'] == ""):
		print 'Serial No. Required'
		sys.exit()

        # Attempt to auto-retrieve hostname
        try:
                factory['factory_host']  = socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
                # Ask user for host
                factory['factory_host'] = raw_input("Host: ")

##
#  device_info() -> Parse arguments and request factory info
##

def device_info():

	# Ask user to specify probe
	factory_probe()

	# Ask user for factory details 
	factory_details()


#---------------------------------------#
#             SCRIPT SETUP              #
#---------------------------------------#

##
#  create_script_prefix() -> Create prefix for all files
##

def create_script_prefix():

	# Set specifier to 'factory_serialno'
	specifier  = factory['factory_serialno']


        # Write 'prefix' to script_info
        script['prefix'] = specifier + '_' + time.strftime("%m.%d") + '_' + time.strftime("%H.%M.%S")

##
#  create_script_folder() -> Create folder for all files
##

def create_script_folder():

        # Retrieve user root folder
        user_folder = os.environ['HOME']

        # Build folder for all instances
        all_folder = user_folder + '/Panics/'

        # Check if folder already exists
        if (not os.path.exists(all_folder)):

                # Create folder
                os.makedirs(all_folder)

        # Builder folder to single instance
        folder = all_folder + script['prefix'] + '/'

        # Verfy script folder does not already exist!
        if (os.path.exists(folder)):
                print 'Script folder exists!'
                sys.exit()

        # Create script folder
        os.makedirs(folder)

        # Print script folder for factory
        print 'Script Folder: ' + folder

        # Write 'folder' to script_info
        script['folder'] = folder

##
#  create_script_log() -> Create file for script log
##

def create_script_log():

        # Create script log
        log = open(script['folder'] + script['prefix'] + '.' + 'script.log', 'w') 
     
        # Write 'log' to script_info
        script['log'] = log

##
#  script_setup()
##

def script_setup():

        # Create prefix for all files
        create_script_prefix()

        # Create folder for all files
        create_script_folder()

        # Create file for script log
        create_script_log()


#---------------------------------------#
#             KERNEL PANIC              #
#---------------------------------------#

##
#  astris_is_panic() -> Run 'astrisctl isPanic'
##

def astris_is_panic():

        # Print for factory 
        print '\nDevice state'

        # Write title to script log
        script['log'].write('\nStarting astris_is_panic()\n')

        # Spawn 'astrisctl isPanic' process
        cmd = ['astrisctl', '--host', target['astris_host'] + ':' + target['astris_probe'], '--force-kick', 'isPanic']
        read_val = proc_spawn(cmd)[0]

        # Parse returned stdin
        for line in read_val:

                # Check if stackshot created
                if ('Saved stackshot' in line):

                        # Set 'stackshot' in panic_info
                        panic['stackshot'] = True

                        # Parse stackshot binary path
                        stackshot_path = line.split()[5]
                        stackshot_name = stackshot_path.split('/')[6]

                        # Spawn 'cp' process to copy stackshot binary data
                        cmd = ['cp', stackshot_path, script['folder'] + stackshot_name]
                        proc_spawn(cmd)

                # Check if device panicked
                if ('Panicked with string:' in line):

                        # Set 'failure' in panic_info 
                        panic['failure'] = 'KERNEL PANIC'

                        # Write panic string to panic_info
                        panic['panic_str'] = read_val[4] 

			# Write 'state' in panic_info
			panic['state'] = 'kernel'

                        # Print for factory
                        print '->KERNEL PANIC'
                        print panic['panic_str']


##
#  kernel_panic() -> Check if device is panicked
##

def kernel_panic():

        # ASTRIS
	astris_is_panic()

#---------------------------------------#
#            DEVICE STATE               #
#---------------------------------------#

##
#   astris_state()
##

def astris_state():

        # Write title to script log
        script['log'].write('\nStarting astris_state()\n')

        # Spawn 'astris' process
        cmd = ['astris', target['astris_host'] + ':' + target['astris_probe'], '--force-kick', '--enable-jtagap=false', '--stdio']
        read_val, target['astris'] = proc_spawn(cmd)

        # Parse returned stdin
        for line in read_val:

                # Check if astris explore failed
                if 'explore failed' in line:

                        # Write 'failure' in 'panic'
                        panic['failure'] = 'EXPLORE FAILED'

                        # Write 'state' in 'panic'
                        panic['state'] = 'exporefailed'

                        # Print for factory
                        print '->EXPLORE FAILED'

                        # File radar with logs
                        sys.exit()

                # Check if Probe Firmware provided
                if 'Probe firmware' in line:

                        # Write 'astris_probefw' in 'target'
                        target['astris_probefw'] = line.split()[2]

                # Check what CPUs are available
                if 'Listening on' in line:

                        # Check if AP CPUs
                        if ('CPU' in line):
				pass

                        # Check if coprocessor:
                        else:
                                if line.split()[5].lower() in coproc:
                                        coproc[line.split()[5].lower()] = True

                # Check if SoC and Rev provided
                if 'Detected' in line:

                        # Write 'soc' in 'panic'
                        panic['soc'] = line.split(' ')[1]

                        # Write 'rev' in 'panic'
                        panic['soc_rev'] = line.split(' ')[2]

	# Stamp astris log with prefix
        cmd = [script['prefix']]
        proc_write(target['astris'], cmd)

        # Retrieve CPU States
        cmd = ['foreach cpu [::astris::console::native::cpu list] {puts -nonewline "$cpu: [::astris::primitive::cpustate $cpu]"; puts " "}; flush stdout']
        read_val = proc_write(target['astris'], cmd)

        # Write 'cpu_states' to 'panic'
        panic['cpu_states'] = read_val[0]

        # Resume all CPUs
        cmd = ['go -cpu all']
        proc_write(target['astris'], cmd)

        # Halt all CPUs
        cmd = ['halt -cpu all']
        read_val = proc_write(target['astris'], cmd)

        # Parse returned values
        for line in read_val:

                # Check for CPU halt errors
                if ('CPU' in line) and ('ASTRIS_ERR_TIMEOUT' in line):

                        # Write 'failure' in 'panic'
                        panic['failure'] = 'CPU HALT ERROR'

                        # Write 'state' in 'panic'
                        panic['state'] = 'cpuhalterror'

                        # Print for factory
                        print '->CPU HALT ERROR'

                        return

        # Check if panicked
        if (panic['failure'] == 'KERNEL PANIC'):
                return

        # Retrieve Architecture
        cmd = ['cpuinfo -arch 0']
        read_val = proc_write(target['astris'], cmd)

        # ARM64 Platforms
        if (read_val[0] == 'ARMV8'):

                # Read size of virtual address TCR_EL1->TTBR[1]
                cmd = ['reg -cpu 0 3,0,c2,c0,2']
                read_val = proc_write(target['astris'], cmd)

                # Check if kernel has booted
                if (int(read_val[0], 16) & 0x3F0000):

                        # Write 'failure' in 'panic'
                        panic['failure'] = 'KERNEL HANG'

                        # Write 'state' in 'panic'
                        panic['state'] = 'kernel'

                        # Print for factory
                       	print '->KERNEL HANG'

                        return


                # EFIDIAGS-ARM64
                cmd = ['mem -memap 4 0x800000008']
                read_val = proc_write(target['astris'], cmd)

                # Check for EFI marker 
                if ('0x9' in read_val[0]):

                        # Write 'failure' in 'panic'
                        panic['failure'] = 'EFI DIAGS'

                        # Write 'state' in 'panic'
                        panic['state'] = 'efidiags'

                        # Print for factory
                        print '->EFI DIAGS'

                        # File radar with logs
                        return

        # NON-ARM64 Platforms
        else:
                # Read transaction table format width TTBCR
                cmd = ['reg -cpu 0 p15,0,c2,c0,2']
                read_val = proc_write(target['astris'], cmd)

                # Check if kernel has booted
                if (int(read_val[0], 16) & 0x7):

                        # Write 'failure' in 'panic'
                        panic['failure'] = 'KERNEL HANG'

                        # Write 'state' in 'panic'
                        panic['state'] = 'kernel'

                        # Print for factory
                        print '->KERNEL HANG'

                        return

                # EFIDIAGS-ARM
                cmd = ['mem -memap 4 0x80010008']
                read_val = proc_write(target['astris'], cmd)

                # Check for EFI marker 
                if ('0x9' in read_val[0]):

                        # Write 'failure' in 'panic'
                        panic['failure'] = 'EFI DIAGS'

                        # Write 'state' in 'panic'
                        panic['state'] = 'efidiags'

                        # Print for factory
                        print '->EFI DIAGS'

                        # File radar with logs
                        return

        # NOT IN KERNEL
        # Write 'failure' in 'panic'
        panic['failure'] = 'NOT IN KERNEL'

        # Write 'state' in 'panic'
        panic['state'] = 'notkernel'

        # Print for factory
        print '->Not in kernel'


##
#   device_state()
##

def device_state():

        # ASTRIS
        if (target['astris_probe'] != 'Unknown'):

		astris_state()

#---------------------------------------#
#               KERNEL                  #
#---------------------------------------#

##
#  kernel_corefile() - Capture kernel corefile
##

def kernel_corefile():

        # Write title to log
        script['log'].write('\nStarting kernel_corefile()\n')

        # Attempt kernel corefile
        cmd = ['coredump -io', script['folder'] + script['prefix'] + '.kernel.core']

        # Run astris coredump command 
        proc_write(target['astris'], cmd)


##
#  kernel() - Handle all kernel related tasks
##

def kernel():

        # ASTRIS
        if (target['astris_probe'] != 'Unknown'):

                # Run Astris kernel coredump
                kernel_corefile()

#---------------------------------------#
#           COPROCESSOR                 #
#---------------------------------------#

##
#  coprocessor_corefile() - Attempt coprocessor corefiles
##

def coprocessor_corefile(proc):

        # Write title to log
        script['log'].write('\nStarting coprocessor_corefile() - ' + proc + '\n')

	# Print status for user
	print '->' + proc

	# Check if proc is NOT s3e
	if (proc != 's3e'):

		# Attempt co_processor corefile
		cmd = ['co_coredump -cpu', proc, script['folder'] + script['prefix'] + '.' + proc + '.core']
		proc_write(target['astris'], cmd)

	else:
		# Halt s3e CPUs
		cmd = ['halt -cpu all']
		proc_write(target['astris'], cmd)

		# Attempt s3_coredump 
		cmd = ['s3_coredump', script['folder'] + script['prefix'] + '_' + proc]
		proc_write(target['astris'], cmd)

		# Go s3e CPUs
		cmd = ['go -cpu all']
		proc_write(target['astris'], cmd)
		
##
#  s3e_bypass() - Attempt to enable or disable s3e bypass
##

def s3e_bypass(val):

        # Write title to log
        script['log'].write('\nStarting s3e_bypass() - ' + str(val) + '\n')

	# Check if enable
	if (val == 1):
		
		# Attempt s3_coredump 
		cmd = ['enable_swd_bypass -force_pins 2']
		read_val = proc_write(target['astris'], cmd)

		# Parse returned values
		for line in read_val:

			# Check if Astris detected auto-gating of NAND sysclk
			if ('auto-gating of NAND sysclk' in line):

				# Keep track of auto-gating
				target['s3e_auto-gate'] = True
				
				# Disable NAND sysclk auto-gating
				cmd = ['nandsysclk_autogate_ctrl off']
				read_val = proc_write(target['astris'], cmd)

				# Attempt s3e_bypass again
				ret = s3e_bypass(1)

				return ret

		# List all CPUs
		cmd = ['::astris::console::native::cpu list']
		read_val = proc_write(target['astris'], cmd)

		# Parse returned values
		for line in read_val:

			# Check if s3e bypass is succesfull
			if ('CPU0 MSP0' in line):

				return True

		# Bypass failed
		return False

	# Check if enable
	if (val == 0):

		# List all CPUs
		cmd = ['::astris::console::native::cpu list']
		read_val = proc_write(target['astris'], cmd)

		# Parse returned values
		for line in read_val:

			# Check if we are bypassed still
			if ('CPU0 MSP0' in line):

				# Attempt s3_coredump 
				cmd = ['disable_swd_bypass']
				proc_write(target['astris'], cmd)

				# List all CPUs
				cmd = ['::astris::console::native::cpu list']
				read_val = proc_write(target['astris'], cmd)

				# Parse returned values
				for line in read_val:

					# Make sure we are no longer bypassed
					if ('CPU0 MSP0' in line):

						# Try disable bypass again
						s3e_bypass(0)

						return
	
				# Check if auto-gate was previously enabled
				if (target['s3e_auto-gate'] == True):

					# Enable NAND sysclk auto-gating
					cmd = ['nandsysclk_autogate_ctrl off']
					read_val = proc_write(target['astris'], cmd)

##
#  coprocessor() - Handle all coprocessor debug tasks
#  Factry -> blocked by rdar://problem/22180178&21737048
##

def coprocessor():

        # Iterate coprocessors
        for proc in coproc:

		# Check if available
		if (coproc[proc] == True):

			# ASTRIS
			if (target['astris_probe'] != 'Unknown'):

				# Run Astris coprocessor coredump
				coprocessor_corefile(proc)

	# Check if s3e available
        if (panic['soc'] in s3e_list):

		# ASTRIS
		if (target['astris_probe'] != 'Unknown'):

			# Enable s3e bypass
			ret = s3e_bypass(1)

			# Check if successful
			if (ret):

				# Run Astris coprocessor coredump
				coprocessor_corefile('s3e')

				# Disable s3e bypass
				s3e_bypass(0)

#---------------------------------------#
#              REPORT                   #
#---------------------------------------#

##
#  save_astris() - Copy relevant astris log
##

def save_astris():

        # Quit Astris
        cmd = ['quit']
        proc_write(target['astris'], cmd)

        # Build astris log directory
        astris_dir = os.environ['HOME'] + '/Library/Logs/Astris'

        # Spawn 'grep' process for astris log
        cmd = ['grep','-r', script['prefix'], astris_dir]
        read_val, proc = proc_spawn(cmd)

        # Get file path to astris log
        file_path = read_val[0].split(':')[0]

        # Spawn 'cp' process for astris log
        cmd = ['cp',file_path, script['folder'] + '.']
        proc_spawn(cmd)

##
#  radar_report() - Write radar info to file
##

def radar_report():

	# Create radar report file
        script['radar_report'] = open(script['folder'] + script['prefix'] + '.' + 'radar.txt', 'w') 
     
        # Print Radar Component
        script['radar_report'].write('\nRADAR COMPONENT\n')
	radar_component = 'Panic Triage | iOS'
        if 'N71' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | N71'
        if 'N66' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | N66'
        if 'N69' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | N69'
        if 'J127' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | J127'
        if 'J128' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | J127'
        if 'J99A' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | J99A'
        if 'J99' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | J99A'
        if 'D10' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | D10'
        if 'D11' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | D11'
        if 'N74' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | N74'
        if 'X527' in factory['factory_build']:
                radar_component = 'Factory Panic Triage | X527'
        script['radar_report'].write(radar_component)

        # Print Radar Title
        script['radar_report'].write('\n\nRADAR TITLE\n')
        radar_title = '[' + factory['factory_build'] + ']' + ' ' + factory['factory_bundle'] + ':' + ' '
        if panic['failure'] == 'KERNEL PANIC':
                radar_title += panic['panic_str']
        else:
                radar_title += panic['failure']
        script['radar_report'].write(radar_title)

        # Print Radar Description
        script['radar_report'].write('\n\nRADAR DESCRIPTION')
        radar_triage = '\nTRIAGE'
        radar_triage += '\nFailure: ' + panic['failure']
        if panic['failure'] == 'KERNEL PANIC': 
                radar_triage += '\n' + panic['panic_str']
        radar_triage += '\nTest: ' + factory['factory_test']
        script['radar_report'].write(radar_triage)

        radar_device = '\n\nDEVICE INFO'
        radar_device += '\nBuild:  ' + factory['factory_build']
        radar_device += '\nBundle: ' + factory['factory_bundle']
        radar_device += '\nConfig: ' + factory['factory_config']
        radar_device += '\nSerialNo: ' + factory['factory_serialno']
        if panic['failure'] != 'Explore Failed':
                radar_device += '\nSoC: ' + panic['soc'] + ' ' + panic['soc_rev']
        script['radar_report'].write(radar_device)

        radar_connect = '\n\nCONNECT'
        radar_connect += '\nFolder: ' + script['folder']
        radar_connect += '\nHostIP: ' + factory['factory_host']
        radar_connect += '\nProbe: ' + target['astris_probe']
        radar_connect += '\nProbeFW: ' + target['astris_probefw']
	radar_connect += '\n\n'
        script['radar_report'].write(radar_connect)

        # Close radar_report file descriptor
        script['radar_report'].close()

        # Close script_log file descriptor
        script['log'].write('Closing log')
        script['log'].close()

##
#  archive_folder() - Archive folder of logs and corefiles
##

def archive_folder():

	# Create archive file
	script['archive'] = script['prefix'] + '.zip'

	# Open zipfile handle
	archive_handle = zipfile.ZipFile(script['folder'] + script['archive'], 'w')
	
	# Walk the script folder
	for dirName, subdirList, fileList in os.walk(script['folder']):

		# Root files
		if (dirName == script['folder']):
			for filename in fileList:
				# Prevent infinite loop
				if (filename != script['archive']):
					# Write file to archive
					archive_handle.write(dirName + filename, arcname = filename)
		# Sub-folders
		else:
			for filename in fileList:
				# Write file to archive
				archive_handle.write(dirName + '/' + filename, arcname = dirName.split('/')[-1] + '/' + filename)

	# Close zipfile handle
	archive_handle.close()

	# Ask user to attach archive
	print '\nPlease attach to radar:'
	print script['folder'] + script['archive'] 


##
#  report() - clean up, print report, file radar*
##

def report():

	# Copy relevant astris log
	save_astris()

	# Print radar info
	radar_report()

	# Archive folder of logs and corefiles
	archive_folder()


#---------------------------------------#
#               START                   #
#---------------------------------------#

# Print version
print 'factorytriage2.py (beta)'

# Retrieve device info
device_info()

# Setup environment
script_setup()

# Check if kernel panic
kernel_panic()

# Retrieve device state
device_state()

# Kernel related tasks
if (panic['state'] == 'kernel'):
	kernel()

# Co-processor related tasks
coprocessor()

# Report
report()

# Finish!
print 'Goodbye!'
