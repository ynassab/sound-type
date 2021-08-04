from playsound import playsound
import multiprocessing as mp
from time import sleep
import argparse


def play_strings(strings):
	num_strings = len(strings)
	pools = [mp.Pool(num_strings) for j in range(len(strings[0]))] # n processes
	for j,note in enumerate(strings[0]):
		pool = pools[j]
		for i in range(num_strings):
			pool.apply_async(play_note, (strings[i][j],))
		pool.close()
		pool.join()


def play_note(note):
	if note == "0":
		sleep(0.35) # rest
	elif note == "1":
		playsound('piano//C4.wav')
	elif note == "2":
		playsound('piano//D4.wav')
	elif note == "3":
		playsound('piano//E4.wav')
	elif note == "4":
		playsound('piano//F4.wav')
	elif note == "5":
		playsound('piano//G4.wav')
	elif note == "6":
		playsound('piano//A4.wav')
	elif note == "7":
		playsound('piano//B4.wav')
	elif note == "8":
		playsound('piano//C5.wav')


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--strings', nargs='*')
	
	args = parser.parse_args()
	play_strings(args.strings)

