with open('input.txt') as f:
    tracks, swaps, idx = f.read().split('\n\n')

idx = int(idx)
tracks = [int(x) for x in tracks.split('\n')]
swaps = [[int(x.split('-')[0]), int(x.split('-')[1])] for x in swaps.split('\n')]
    
for i, verta in enumerate(swaps):
    ix = verta[0]-1
    iy = verta[1]-1
    iz = swaps[i+1][0]-1 if i < len(swaps)-1 else swaps[0][0]-1
    a = tracks[ix]
    b = tracks[iy]
    c = tracks[iz]
    tracks[iy] = a
    tracks[iz] = b
    tracks[ix] = c
    
print(f'Part 2: {tracks[idx-1]}')