with open('input.txt') as f:
    tracks, swaps, idx = f.read().split('\n\n')

idx = int(idx)
tracks = [int(x) for x in tracks.split('\n')]
swaps = [[int(x.split('-')[0]), int(x.split('-')[1])] for x in swaps.split('\n')]
    
for swap in swaps:
    a = tracks[swap[0]-1]
    b = tracks[swap[1]-1]
    tracks[swap[0]-1] = b
    tracks[swap[1]-1] = a
    
print(f'Part 1: {tracks[idx-1]}')