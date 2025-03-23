with open('input.txt') as f:
    tracks, swaps, idx = f.read().split('\n\n')

idx = int(idx)
tracks = [int(x) for x in tracks.split('\n')]
swaps = [[int(x.split('-')[0]), int(x.split('-')[1])] for x in swaps.split('\n')]
    
for i, verta in enumerate(swaps):
    ix = verta[0]-1
    iy = verta[1]-1
    lenblock = min(len(tracks) - max(ix, iy), abs(ix - iy))
    for i in range(lenblock):
        a = tracks[ix+i]
        b = tracks[iy+i]
        tracks[ix+i] = b
        tracks[iy+i] = a
        
    
print(f'Part 3: {tracks[idx-1]}')