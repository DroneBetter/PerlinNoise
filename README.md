# PerlinNoise
Program for experimenting with Perlin noise, overlays different vector field densities (and can spherise to hemisphere with `s` key).

## Web version
[Here](https://turbowarp.org/569387624)

## Controls
Green flag to generate new noise, `r` to re-render (seems broken currently), 's' to spherise (only render pixels within the screen square's inscribed circle), `n` to view each node's brightness as the number of neighbours it exceeds, `m` to view each as the sum of differences from neighbours (not very good), `j` and `k` are the same as `n` and `m` except each neighbour's addition to a pixel is coloured (up is red, down is cyan, like a colour wheel) for domain colouring, `k` isn't very good (it looks like contour lines, not sure why), but `j` is. Hold `i` while rerendering to subtract distance from outputs to make an island in the centre.
<img width="996" alt="image" src="https://user-images.githubusercontent.com/58664547/132987491-a9ee8439-c20d-43fb-b3fa-cd6ed785b097.png">
8\*8 vector field noise
<img width="996" alt="image" src="https://user-images.githubusercontent.com/58664547/132987506-0fe2d370-78e9-4c8d-8f21-2f9421b9ffa4.png">
Overlaid outputs of fields increasing from 8^2 to 256^2.
<img width="996" alt="image" src="https://user-images.githubusercontent.com/58664547/132987574-7fdca014-9957-4be3-9f13-1e217b54ab7c.png">
Another 8\*8 field but with nodes displayed as neighbours exceeded.
<img width="996" alt="image" src="https://user-images.githubusercontent.com/58664547/132987555-a50a17b7-1c33-451d-9957-cec17330f97d.png">
That but with domain colouring.
<img width="996" alt="image" src="https://user-images.githubusercontent.com/58664547/132987627-cd853bfd-177f-42b7-bc61-05edbee6e419.png">
A planet with altitude mapping.
