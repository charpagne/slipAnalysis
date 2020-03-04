# slipAnalysis
This code calculates and plots schmid factors, plane traces and opening angles in a deformed sample
Load your grain file in .txt format from TSL OIM or other
Pick a grain and a lattice (e.g. BCC), the programm will:
  - compute all Schmid factors, plot and save them
  - compute all plane traces, plot and save them
  - compute all opening angles in the reference frame of the slip band, and save them
Conventions: loading direction = horizontal (message me if you'd like me to make it a parameter of the code)
Euler angles = Bunge's convention (angles are all in degrees, though there's a function in crystallography.py you can change to convert them if needed, message me if you'd like this to be a parameter in the code)

## How to
Download both files and change the path to your grain file.
You want to edit the analyzeGrain.py file only:
  - 1/ pick your lattice
  - 2/ pick your grain # of interest
  - 3/ hit 'run'
nb: You can also change the heading and infer directly your Euler angles.

## Example
Here's an example of the code's output, for a grain of Euler angles (194.3,83.2,68.1) in a BCC lattice, grain '48' in 'grainFile2.txt'

### Schmid factors
Schmid factors for {110} planes:
![grain_48_sf_110](https://user-images.githubusercontent.com/33326429/75932449-435d9580-5e2c-11ea-9b26-6374786cd0b0.png)
{112} planes:
![grain_48_sf_112](https://user-images.githubusercontent.com/33326429/75932592-b109c180-5e2c-11ea-9ee8-8b7657db0f44.png)
{123} planes:
![grain_48_sf_123](https://user-images.githubusercontent.com/33326429/75932631-c7178200-5e2c-11ea-8827-2fb1c1344a26.png)
{134} planes:
![grain_48_sf_134](https://user-images.githubusercontent.com/33326429/75932642-cf6fbd00-5e2c-11ea-8cc9-82a74e2e9ce2.png)

### Plane traces
Traces of {110} planes:
![grain48_traces_110](https://user-images.githubusercontent.com/33326429/75932676-e31b2380-5e2c-11ea-9c26-1f5b98ecb113.png)
{112} planes:
![grain48_traces_112](https://user-images.githubusercontent.com/33326429/75932714-f9c17a80-5e2c-11ea-933b-bc1afc5f8f2d.png)
{123} planes:
![grain48_traces_123](https://user-images.githubusercontent.com/33326429/75932719-004ff200-5e2d-11ea-84cf-c6e6dc850acf.png)
{134} planes:
![grain48_traces_134](https://user-images.githubusercontent.com/33326429/75932727-06de6980-5e2d-11ea-8fcd-47e19f7dbb9f.png)

### Gamma angles
Opening ('gamma') angles are to be considered when you are using a discontinuity-tolerant DIC code (e.g. Heaviside DIC, as in F. Bourdin, JC. Stinville et al., Measurements of Plastic Localization by Heaviside-Digital Image Correlation, Acta Materialia 157, pp.307:325 (2018), doi: 10.1016/j.actamat.2018.07.013, https://www.researchgate.net/publication/326406014_Measurements_of_Plastic_Localization_by_Heaviside-Digital_Image_Correlation).
This angle is calculated in the reference frame of the slip band and enables to determine the slip direction among discrete possibilities, once the slip plane is known. See above publication for more details, as well as MA. Charpagne, JC. Stinville et al. Materials Characterization (2020), details to come.
Convention for the gamma angle:
![additionalFigure](https://user-images.githubusercontent.com/33326429/75933549-1b236600-5e2f-11ea-8133-73c6fafcbe04.jpg)
(see above publication for more details).
Gamma angles are saved in a .txt file when you run the code.
