def onename(option,name,pids,names):
    def pidstr_to_integer(pid_string):
        pid = pid_string.strip()
        try:
            return int(pid)

        except:
            pass

    if option != 5:
        pass

    else:

        name += (25 - len(name)) * ' '
        names, pids = names[1:], pids[1:]
        names_number = names.count(name) # number of names
        lenght = len(names) == len(pids), len(names)
        kill_list = [] # list of pid's to kill
        i=0
        pid = None

        if names_number > 0 and option == 5:
            for name_ in names:
                pid = pids[i]
                i+=1
            
                if name_ == name:
                    pid_to_kill = pidstr_to_integer(pid)
                    kill_list.append(pid_to_kill)
        
            return kill_list

import os, sys, platform

# pin: Proccess Identification Number
# pid: Proccess ID or Proccess Identification
# pn: Process Name (proccess name only without the extension)
# pcn: Proccess Complete Name (complete name of the proccess)
# apsn: All Programs Same Name (all programs with one/same name)

# checks the running Operating System
def os_checking():
    system = 'Windows'
    os = [list(platform.uname())[0],platform.platform()]
    os = os[1][:7],os[0]
    boolean = os[0] == os[1]
    guess = os[0] == system or os[1] == system
    o_s = os[0] == system and os[1] == system
    if boolean is True and o_s is True:
        pass # operating system checked successfully

    elif guess == True:
        print('problem checking operating system, the tool may run incorrectlly')

    else:
        sys.exit('operating system must be windows')


# converts number in string type to integer type
def int_convert(value,code):
    if len(str(value)) > 0:
        pass
    else:
        sys.exit(f"error: received value is empty, try again with a value")
 
    try:
        try:
            if code != 3 and code != 4 and code != 5:
            # excepting 3, 4 and 5, because of these are non number options or strings characters options
                return int(value) # return converted string to integer
            else:
                # if it's not a number, it's letters(string chars), returns the letters(string chars) itself
                return value

        except:
            pass

    except Exception as err:
        pass

def kill_proccess(option,signterm,value,numbers,names,pids):

    try:
        if signterm == 15:
            signterm = "" # this option terminates the program but wihtout forcing it 
        elif signterm == 9:
            signterm = " /f " # this option forces the program to stop 
        else:
        # if signterm code is not valid or unknown, exits the tool
            sys.exit(f"error: wrong signterm code")

        if option == 1:
        # option one, PIN option (proccess identification number)
            pid = int_convert(numbers[value],1) # converts pid returned in the function to integer type
            command = f"taskkill{signterm}/pid {pid}"
            os.system(command)

        elif option == 2:
        # option two, PID option (proccess identification)
            command = f"taskkill{signterm}/pid {value}"
            os.system(command)

        elif option == 3:
        # option three, PN option (program name)
            # if given value is greatter than four characters
            if len(value) > 4:
            # check if the lasts four characters are '.exe'
                exe_check = value[-4] + value[-3] + value[-2] + value[-1]
                if exe_check != '.exe':
                # if the lasts four characters are not '.exe'
                    value = value + ".exe" # appends '.exe' extension th the (value/name/proccess name given)
                    pid = names[value] # gets the pid with 'proccess name' as velue
                    command = f"taskkill{signterm}/pid {pid}"
                    os.system(command)

                else:
                # if the lasts four characters are '.exe'
                    pid = numbers[value] # gets the pid (using proccess name as key)
                    command = f"taskkill{signterm}/pid {pid}"
                    os.system(command)

            else:
            # if the given value is not greatter than four, if it's less than four 
                pid = numbers[value] # gets the pid directly with the given value (cause it can be a proccess name without .exe extension or something like that)
                command = f"taskkill{signterm}/pid {pid}"
                os.system(command)

        elif option == 4:
        # option four, PCN option (program complete name or complete proccess name)
            pid = names[value] # gets the pid using given value as key (is waited that the given value / 'complete proccess name' is correctly)
            command = f"taskkill{signterm}/pid {pid}"
            os.system(command)

        elif option == 5:
            input(f"there's {len(pids)} pids that are: {pids}")
            for pid in pids: #pidlist
                pid = int_convert(pid,0)
                command = f"taskkill{signterm}/pid {pid}"
                os.system(command)
                #print("command:",command)

        else:
        # choiced option is invalid
            sys.exit(f"error: wrong option code {option}")

    except Exception as error:
        sys.exit(error)

# (this function) do all the action of getting and managing the proccess's
def proccess():
    try:
        nn=0
        numbers = {} # this dict stores 'pin' as key and 'pid' as value (all pin's and pid's)
        max = 34 # (number) total of bytes of IMAGE NAME and PID part (of output of tasklist command)
        min = 26 # (number) total of bytes of IMAGE NAME part in output of tasklist command (total bytes of IMAGE NAME part without PID part)
        pids = []
        number = 0
        proccess_names = []
        data = os.popen("tasklist").read()
        line, lines = '',[] # each line of all proccess line, and all lines of all proccess lines (each line(string), and all lines(list))
        n = -3 # pin counter to work after 'number' var stops (this -3 stands for the first three lines in 'tasklist' command output, these first 3 lines are not necessary so we jump it and go directly to the proccess's)
        for character in data:
        # for each character in system proccess's strings
            line += character
            if character == '\n':
 
                lines.append(line)
                number += 1
                n +=1 # keep incrementing like 'number' var, also/so/cause it comes to help the 'number' var
                proccess_pid = line[min:max] # it takes just PID part only (takes it from each line of tasklist command output)
                proccess_name = line[:25] # proccess name, taked betwen the start of the line until the first white_space found

                if number == 3:
                # if counter variable is equal to one
                    pids = []
                    numbers = {}
                    lines = []
                    proccess_names = []

                proccess_names.append(proccess_name)
                pids.append(proccess_pid)
                numbers[n] = proccess_pid # 'numbers' dict, with 'n' var as key, and proccess 'pid' as value
                line = ""
                nn+=1

            else:
            # if character is not equal to break line '\n' just keep adding/appending character to 'line' variable
                pass

        n=0 # pin auxiliary var (variable that represents pin)
        print("PIN ==== ====== PCN ==================  PID=Session Name ======= Session == Mem Usage",end="\n\n")
        for each_line in lines:
        # for each line in all lines (proccess info's separeted in lines)
            n+=1 # a variable to print as pin value (pin value part)
            str_n = str(n) # converts counter variable 'n' to string type
            buffer_n = (8-len(str_n)) * " " # 8 is the number of PIN buffer, (bytes reserved to store PIN number)
            buffer_n = str_n + buffer_n # completes counter var with complete buffer of 8 bytes
            print(f"{buffer_n} {each_line}",end="") # prints pin, and a complete line of proccess
        
        return numbers, pids, lines, proccess_names

    except Exception as error:
        sys.exit(error)

    except:
        sys.exit()

def user_input():
    print('1.PIN, 2.PID, 3.PN, 4.PCN, 5.APSN; and signterm: 9. force kill, 15. terminates/kill')
    try:

        user_option = input("option: ").strip()

        signterm = input("signterm: ").strip()

        if user_option == '1':
            proccess_number = input("proccess id number: ")
            return 1, signterm, proccess_number

        elif user_option == '2':
            proccess_id = input("proccess id: ")
            return 2, signterm, proccess_id

        elif user_option == '3':
            proccess_name = input("proccess name: ")
            return 3, signterm, proccess_name

        elif user_option == '4':
            proccess_complete_name = input("proccess complete name: ")
            return 4, signterm , proccess_complete_name

        elif user_option == '5':
            one_name = input("the proccess name: ")
            return 5, signterm, one_name

        elif signterm != '9' and signterm != '15':
        # if choiced signterm codes aren't 9 or 15, exits the tool
            # wrong signterm code
            sys.exit(f"signterm must be 9 or 15")

        else:
            # exits the tool, bacause the choiced option is invalid
            sys.exit("choice option 1 to 4 only")

    except Exception as error:
        sys.exit(error)


# (this function) checking if operating system is windows
os_checking()

# (this function) takes and (treat)proccess (all)the proccess
pin_pid, pids, proccess_lines, proccess_names = proccess()

# user data inputs
option, signterm, value = user_input()

# if is string number converts it to a integer number
value = int_convert(value,option)

# converts signalterm string number to a integer type
signterm = int_convert(signterm,0)

pids_list = onename(option, value,pids, proccess_names)

# (this function) kills the proccess
kill_proccess(option,signterm,value,pin_pid,pids,pids_list)
