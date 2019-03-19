import dataWriterReader

reader = dataWriterReader.Reader()

print(reader.getSpecificSpotifyShortcut('0').text)
print(reader.getSSSbyTag('play').text)
print(reader.getSSHbyTag('open').text)
print(reader.setShortcut('0', 'neii'))
'''print(reader.getSpecificSpotifyShortcut('2'))
print(reader.getSpecificSpotifyShortcut('4'))
print(reader.getSpecificSpotifyShortcut('6'))
print(reader.getSpecificSpotifyShortcut('8'))
print(reader.getSpecificSpotifyShortcut('1'))
'''


