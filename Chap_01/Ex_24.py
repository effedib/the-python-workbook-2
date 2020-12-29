# Units of Time

days, hours, minutes, seconds = input("Inserisci il tempo: ").split()
days, hours, minutes, seconds = [int(days), int(hours), int(minutes), int(seconds)]
days = days * 24
hours = ((hours + days) * 60)
minutes = ((minutes + hours) * 60)
seconds = seconds + minutes
print("Tempo in secondi:", seconds)