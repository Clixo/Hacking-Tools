echo -n "Enter the IP Address or IP Range you want to scan: "
read ip
echo -e "************************************** \nBegin Host Discovery Scan - Ping Sweep \n**************************************" >> hosts.txt
nmap -sn -oG - $ip | awk '/Up$/{print $2}' >> hosts.txt >> hosts.txt
echo -e "*********************************** \nBegin Host Discovery Scan - No Ping \n***********************************" >> hosts.txt
nmap -n -sn -PS22,135,443,445 -oG - $ip | awk '/Up$/{print $2}' >> hosts.txt
echo -e "***************************************** \nBegin Host Discovery Scan - DNS Discovery \n*****************************************" >> hosts.txt
nmap -sS -sU -p53 -oG - $ip | awk '/53\/open/ {print $2}' >> hosts.txt