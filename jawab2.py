# Marhani Wiji Ayu K - 5200411123
# Penjadwalan Round Robin

# Function untuk menemukan waiting time
def findWaktuTunggu(processes, n, burst, wt, kuantum):
	rem_burst = [0] * n
	for i in range(n):
		rem_burst[i] = burst[i]
	t = 0 #saat ini

	while(1):
		done = True
		for i in range(n):
			if (rem_burst[i] > 0) :
				done = False # pending process
				if (rem_burst[i] > kuantum) :
					t += kuantum
					rem_burst[i] -= kuantum
				else:
					t = t + rem_burst[i]
					wt[i] = t - burst[i]
					rem_burst[i] = 0
				
		if (done == True):
			break
			
def findWaktuTurnAround(processes, n, burst, wt, tat):
	for i in range(n):
		tat[i] = burst[i] + wt[i]

def findWaktuRata(processes, n, burst, kuantum):
	wt = [0] * n
	tat = [0] * n

	findWaktuTunggu(processes, n, burst, wt, kuantum)

	findWaktuTurnAround(processes, n, burst, wt, tat)

	print("Processes Burst Time	 Waktu Tunggu","Waktu Turn-Around")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", burst[i],"\t\t", wt[i], "\t\t", tat[i])

	print("\nRata-rata Waktu Tunggu = %.5f "%(total_wt /n) )
	print("Rata-rata Turn Around Time = %.5f "% (total_tat / n))
	
if __name__ =="__main__":
	
	proc = [1, 2, 3]
	n = 3

	burst_time = [15, 7, 10]

	kuantum = 4;
	findWaktuRata(proc, n, burst_time, kuantum)