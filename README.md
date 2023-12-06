<h1 align="center">
 <img src="https://user-images.githubusercontent.com/45159366/129494677-0341843b-c78c-4027-8a2c-43e98a995f6f.png">
  <br />
 Photogrammetry Guide
</h1>

<a href="https://github.com/mikeroyal?tab=followers">
         <img alt="followers" title="Follow me on Github for Updates" src="https://custom-icon-badges.demolab.com/github/followers/mikeroyal?color=236ad3&labelColor=1155ba&style=for-the-badge&logo=person-add&label=Follow&logoColor=white"/></a> 

![Maintenance](https://img.shields.io/maintenance/yes/2023?style=for-the-badge)
![Last-Commit](https://img.shields.io/github/last-commit/mikeroyal/photogrammetry-guide?style=for-the-badge)

         
#### A guide covering Photogrammetry including the applications, libraries and tools that will make you a better and more efficient Photogrammetry development.

**Note: You can easily convert this markdown file to a PDF in [VSCode](https://code.visualstudio.com/) using this handy extension [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf).**

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/129494681-984945b8-9633-4eb1-9f9e-7b4cdd592b5e.png">
  <br />
</p>


# Table of Contents

1. [Getting Started with Photogrammetry](https://github.com/mikeroyal/Photogrammetry-Guide#getting-started-with-photogrammetry)
    - [Types of Photogrammetry](#types-of-photogrammetry)
    - [Photogrammetry Techniques](#photogrammetry-techniques)
    - [Cameras For Photogrammetry](#cameras)
    - [Types of Drones](#drones)
    - [Geographic Information System](#geographic-information-system)
    - [Remote Sensing ](#remote-sensing)
    - [Point Cloud Processing](#point-cloud-processing)
    - [LiDAR](#lidar)
        - [Basic matching algorithms](#basic-matching-algorithms)
        - [Semantic segmentation](#semantic-segmentation)
        - [Ground segmentation](#ground-segmentation)
        - [Simultaneous localization, mapping, SLAM/LIDAR-based odometry; or mapping LOAM](#simultaneous-localization-and-mapping-slam-and-lidar-based-odometry-and-or-mapping-loam)
        - [Object detection and object tracking](#object-detection-and-object-tracking)
    - [Neural Radiance Field (NeRF)](#neural-radiance-field-nerf)
    - [Certifications & Courses](https://github.com/mikeroyal/Photogrammetry-Guide#Certifications--Courses)
    - [Books/eBooks](https://github.com/mikeroyal/Photogrammetry-Guide#BookseBooks)
    - [YouTube Tutorials](https://github.com/mikeroyal/Photogrammetry-Guide#YouTube-Tutorials)

2. [Photogrammetry Tools, Libraries, and Frameworks](https://github.com/mikeroyal/Photogrammetry-Guide#photogrammetry-tools-libraries-and-frameworks)

3. [Autodesk Development](https://github.com/mikeroyal/Photogrammetry-Guide#autodesk-development)

4. [LiDAR Development](https://github.com/mikeroyal/Photogrammetry-Guide#lidar-development)

5. [Game Development](https://github.com/mikeroyal/Photogrammetry-Guide#game-development)

6. [Machine Learning](https://github.com/mikeroyal/Photogrammetry-Guide#machine-learning)

7. [Python Development](https://github.com/mikeroyal/Photogrammetry-Guide#python-development)

8. [R Development](https://github.com/mikeroyal/Photogrammetry-Guide#r-development)


# Getting Started with Photogrammetry 

[Back to the Top](#table-of-contents)

[Photogrammetry](https://www.autodesk.com/solutions/photogrammetry-software) is the art and science of extracting 3D information from photographs. The process involves taking overlapping photographs of an object, structure, or space, and converting them into 2D or 3D digital models. Photogrammetry is often used by surveyors, architects, engineers, and contractors to create topographic maps, meshes, point clouds, or drawings based on the real-world.

## Types of Photogrammetry

* [Aerial photogrammetry](https://www.autodesk.com/solutions/photogrammetry-software) is process of utilizing aircrafts to produce aerial photography that can be turned into a 3D model or mapped digitally. Now, it is possible to do the same work with a drone.

 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/de6208aa-082d-4c75-8b24-54cff3dab78c">
</br>
</p>

Image credit: [Forestrypedia](https://forestrypedia.com/photogrammetry-definitions/)

 * [Terrestrial (Close-range) photogrammetry](https://www.autodesk.com/solutions/photogrammetry-software) is when images are captured using a handheld camera or with a camera mounted to a tripod. The output of this method is not to create topographic maps, but rather to make 3D models of a smaller object.

 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/11aecb3d-5488-4b08-8928-0df569871acb">
</br>
</p>

Image credit: [TLT Photography](https://www.tlt.photography/2018/06/trail-mapping-with-terrestrial-photogrammetry-a-funny-tale/)

 * [Stereo Photogrammetry](https://pro.arcgis.com/en/pro-app/latest/help/analysis/image-analyst/introduction-to-stereo-mapping.htm) is a process that involves the estimation of 3D coordinates of points on an object by considering the measurements made of two or more images taken from different positions. The sensor looks at angles that are horizontal or oblique to collect accurate, detailed information for primarily engineering purposes, such as mapping the infrastructure of bridges, buildings, and dams.

 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/b04d0a9a-b0dd-46cf-9141-fc7fc6e3fbcb">
</br>
</p>

Image credit: Stereo Photogrammetry Capture. [HELImetrex](https://www.helimetrex.com.au/aerial-survey-mapping/stereo-photogrammetry-capture/)

## Photogrammetry Techniques

[Back to the Top](#table-of-contents)

* [Structure from motion (SfM)](https://en.wikipedia.org/wiki/Structure_from_motion) is a photogrammetry range imaging technique for estimating 3D structures from 2D image sequences that may be coupled with local motion signals. 

 * [Scale-Invariant Feature Transform (SIFT)](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) is a computer vision algorithm to detect, describe, and match local features in images. This includes object recognition, robotic mapping and navigation, image stitching, and 3D modeling.
 
 * [Digital Outcrop Model (DOM)](https://en.wikipedia.org/wiki/Digital_outcrop_model) is a digital 3D representation of the outcrop surface, mostly in a form of textured polygon mesh. This allows for interpretation and reproducible measurement of different geological features, orientation of geological surfaces, width, and thickness of layers.
 
 * [DEM (Digital Elevation Models)](https://gisgeography.com/dem-dsm-dtm-differences/) is a bare-earth raster grid referenced to a vertical datum. When you filter out non-ground points such as bridges and roads, you get a smooth digital elevation model. The built (power lines, buildings, and towers) and natural (trees and other types of vegetation) aren’t included in a DEM.
    
 * [DSM (Digital Surface Models)](https://gisgeography.com/dem-dsm-dtm-differences/) is a process that captures both the natural and built/artificial features of the Earth’s surface.
    
* [DTM (Digital Terrain Models)](https://gisgeography.com/dem-dsm-dtm-differences/) is a process that has two definitions depending on where you live. [USGS LiDAR Base Specification](http://pubs.usgs.gov/tm/11b4/pdf/tm11-B4.pdf).

   - In some countries, a DTM is actually synonymous with a DEM. This means that a DTM is simply an elevation surface representing the bare earth referenced to a common vertical datum.
    
   - In the United States and other countries, a DTM has a slightly different meaning. A DTM is a vector data set composed of regularly spaced points and natural features such as ridges and breaklines. A DTM augments a DEM by including linear features of the bare-earth terrain.

 * [TIN (Triangular Irregular Networks)](https://desktop.arcgis.com/en/arcmap/latest/manage-data/tin/fundamentals-of-tin-surfaces.htm) is a representation of a continuous surface consisting entirely of triangular facets (a triangle mesh ), used mainly as Discrete Global Grid in primary elevation modeling. TINs are a form of vector-based digital geographic data and are constructed by triangulating a set of vertices (points). The vertices are connected with a series of edges to form a network of triangles. There are different methods of interpolation to form these triangles, such as Delaunay triangulation or distance ordering.
    
 * [Canopy Height Model (CHM)](https://geodetics.com/dem-dsm-dtm-digital-elevation-models/) is a separate model derived from elevation data in the point cloud. In forested areas, the difference between the DSM and the DEM can be viewed as CHM, representing the height of trees in the area above ground-level. Software utilizing CHMs can also derive individual tree data, such as crown diameter, crown area and tree boundaries. 

 * [Ground Control Points (GCPs)](https://www.usgs.gov/landsat-missions/ground-control-points) is a technique with known real-world coordinates that can be clearly identified in an image. GCPs are used in the orthorectification process to augment the geometric parameters embedded in the raw image and improve the accuracy of the resulting orthorectification. 
 
 * [Orthorectification](https://locationiq.com/glossary/orthorectification) is a process of removing distortion from an image caused by the curvature of the Earth and changes in terrain. It involves correcting the perspective of the image to align it with a map or a coordinate system, resulting in a more accurate representation of the Earth's surface.
 
 * [Orthorectified imagery](https://www.esri.com/about/newsroom/insider/what-is-orthorectified-imagery/) is a type of imagery that has been processed to apply corrections for optical distortions of satellite/aerial imagery caused by topography and sensor geometry errors.
 
  * [Real Time Kinematic (RTK)](https://en.wikipedia.org/wiki/Real-time_kinematic_positioning)  is a satellite navigation technique used to enhance the precision of position data derived from satellite-based positioning systems (global navigation satellite systems, GNSS) such as GPS, GLONASS, Galileo, NavIC and BeiDou. 
  
  * [Post Processing Kinematic (PPK)](https://docs.emlid.com/reach/tutorials/basics/ppk-introduction/) is an alternative a satellite navigation technique to Real-Time Kinematic (RTK) used in surveying that corrects the location data after it is collected and uploaded. This technique is commonly used in drone mapping and land surveying.
  * [Gaussian Splatting](https://huggingface.co/blog/gaussian-splatting) is a rasterization technique described in 3D Gaussian Splatting for Real-Time Radiance Field Rendering that allows real-time rendering of photorealistic scenes learned from small samples of images. [Polycam Gaussian splat viewer and creator](https://poly.cam/gaussian-splatting)
 * [DynIBaR (Neural Dynamic Image-Based Rendering)](https://dynibar.github.io/) is a new method that generates photorealistic free-viewpoint renderings from a single video of a complex, dynamic scene. It can be used to generate a range of video effects, such as “bullet time” effects (where time is paused and the camera is moved at a normal speed around a scene), video stabilization, depth of field, and slow motion, from a single video taken with a phone’s camera. [DynIBaR: Space-time view synthesis from videos of dynamic scenes | Google Research](https://blog.research.google/2023/09/dynibar-space-time-view-synthesis-from.html)

## Cameras

[Back to the Top](#table-of-contents)

<p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/f2189325-c52b-40c2-867d-1b859f059ede">
</br>
DJI Zenmuse P1 Full-frame 45MP camera.
</p>

**Links to Helpful Resources:**

 * A great resource for everything to do with cameras: https://www.dpreview.com/.
 * [Automatic 360° HDRI camera for photogrammetry | Civetta - Weiss AG](https://weiss-ag.com/civetta360camera/)
 * [The Best Photogrammetry Solutions in 2023 - XR Today](https://www.xrtoday.com/mixed-reality/the-best-photogrammetry-solutions-in-2023/)
 * [Low-Cost Cameras for Photogrammetry and Measurement (Price range:$750 and $1200)](https://www.photomodeler.com/low-cost-cameras-for-photogrammetry/)
 * [Which Camera to Use with Photogrammetry and PhotoModeler](https://www.photomodeler.com/products/about_cameras/)
 * [How To Pick The Best Camera For Drone Photogrammetry](https://www.heliguy.com/blogs/posts/how-to-pick-the-best-camera-for-drone-photogrammetry)
 * [Best Camera For Photogrammetry In 2023 (Top 10 Models) - GetPhotography](https://getphotokits.com/best-camera-for-photogrammetry/)
 

#### General camera-type recommendations

**Here are some categories in which you should start your research:**

<p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/2ab5e909-e5bc-4994-bee8-29f3f26557a8">
</br>
Camera Photogrammetry Nikon D300/5mm precision GPS setup for VORTEX2. Image credit: NOAA
</p>

#### Fully automatic operation:

  * **Default:** high-end phone.

  * **Some more flexibility in a zoom range:** high-end compact camera (as in the Sony RX100 line).

  * **More flexibility, including distant subjects:** high-end superzoom camera (as in the Sony RX10 and Panasonic FZ1000 lines).

  * **Extremely distant subjects in daylight:** consumer superzoom camera (as in the Nikon P line, Panasonic FZ80, etc.).

#### Manual/creative control:

  * Default: mirrorless camera.

  * Cheaper alternative (no mirrorless camera that suits your needs is available under budget): DSLR.

    If you’re absolutely sure that’s the only lens you’ll need: fixed prime lens camera (as in the [Fujifilm X100](https://fujifilm-x.com/products/cameras/x100v/) and [Ricoh GR lines](https://us.ricoh-imaging.com/product/gr-iii/)), high-end compact camera or high-end superzoom camera.

#### Key concepts and terminology

There are some concepts, terms and features of a camera that you’ll need to learn about to really understand camera reviews and see how one camera differs from another. The following is a list of such terms for you to look up if needed.

<p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/af3bd5c1-32e1-45fe-9e18-bbf413d3cd56">
</br>
Camera Basics. Image credit: Geodetic Systems, Inc
</p>

  * Exposure, noise, dynamic range (SDR and HDR).

  * **Camera design:** interchangeable-lens cameras and fixed-lens cameras, mirrorless and DSLR.

  * **Image sensor:** size and surface area, resolution.

  * **Lens:** focal length and angle/field of view, maximum aperture, lens mount and format coverage.

  * Autofocus.

  * Continuous/burst shooting, buffer depth.

  * Viewfinder and display.

  * Image stabilization.

  * Weather resistance.

Remember a camera’s age is irrelevant. Cameras don’t age like smart phones or computers do, because they have no increasingly demanding software to keep up with. So as long as a camera is in good working order, it should work as well as it did when it was brand new.

Make sure to shop at well accepted and well established in the camera market, even at the high end. Try reputable outlets ([KEH](https://www.keh.com/) and [mpb](https://www.mpb.com/)) and the used sections on big retailers ([B&H](https://www.bhphotovideo.com/) and [Adorama](https://www.adorama.com/) in the US) and local camera stores. You can also find refurbished cameras sold directly by the manufacturers’ distributors. 

## Drones

[Back to the Top](#table-of-contents)

**Links for Drone photography:**

  * [Drone photography: A beginner's guide - Adobe](https://www.adobe.com/creativecloud/photography/discover/drone-photography.html)
  * [Drone Photography: Beginner's Guide to Getting Started - Droneblog](https://www.droneblog.com/drone-photography/)
  * [The complete beginner's guide to drone photography - Canva](https://www.canva.com/learn/the-complete-beginners-guide-to-drone-photography/)
  * [Drone Photography: The Definitive Guide (2023) | PhotoPills](https://www.photopills.com/articles/drone-photography-guide)
  * [19 Drone Photography Tips to Improve Your Aerial Shots in 2023](https://shotkit.com/drone-photography-tips/)
  * [Drone photography: Tips and tricks | Space](https://www.space.com/guide-to-drone-photography)

A drone is basically an Unmanned Aerial Vehicle (UAV). Before the rise in consumer interest in UAVs, the word “drone” was primarily used to refer to the UAVs used by the military.

Now, though, intelligent quadcopters that have UAV-like features are more popular among consumers than ever before. And while they technically aren’t as advanced as military drones, we refer to them as ”drones” because they are similar in nature (both allow you to operate an aerial vehicle in order to perform a particular task, which, in the case of consumer drones, is typically to shoot video or capture still images).

 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/0e59e19d-fbce-490e-8876-de9deaac6272">
</br>
</p>

There are different types of drones for all kinds of situations, so make sure to consider the main purpose for your drone purchase. Even though most drones fall under the categories of consumer or professional grade drones, there are now UAVs geared towards traveling and selfies.

 * **Camera drones:** These drones might range from $100 to $1000 which have exceptional features that make such drones a market leader in the world of professional drones. They also have Obstacle avoidable sensors.

 * **Compact drones:** These drones are specially designed for panoramic images and landscape shoot. The best feature of compact drones is that they have an ability to change the image format from JEPG to raw images. Raw images have more details and can produce 4k quality of the picture and videos. For example, [DJI Inspire 2](https://www.dji.com/inspire-2), which falls in the category of professional drones has a speed of 60+ miles per hour (97+ kilometers per hour) and has a dual battery backup of up to 30 minutes. Use these drones in the places where you cannot step in and take the pictures that you don’t need to crop or it can adversely affect the quality of the picture.

**The different among RTF, BNF and ARF:**

  * **RTF stands for Ready-To-Fly** - Usually an RTF quadcopter doesn’t require any assembly or setup, but you may have to do some simple things like charge up the battery, install the propellers or bind the controller to the quadcopter (get them talking to each other).

  * **BNF stands for Bind-And-Fly** - A BNF quadcopter usually comes completely assembled, but without a controller. With BNF models, you’ll have to use the controller that you already have (if it’s compatible) or find a controller sold separately. One thing you should know is that just because a transmitter and receiver are on the same frequency that doesn’t mean that they’ll work together.

  * **ARF stands for Almost-ready-to-fly** - ARF Drones are usually like quadcopter kits. They usually don’t come with a transmitter or receiver and might require partial assembly. An ARF drone kit might also leave out components like motors, ESCs, or even the flight controller and battery. The definition of an ARF drone kit is very broad, so whenever you see ARF in the title, you should read the description thoroughly.

### Taking care of legal consideration

Before you get started with your drone (I know you must be excited) make sure you are updated with all the rules and regulations for what you can and what you cannot do with the drone, the restricted areas and the permission to fly near any private property.

 * Various countries have their own rules and regulations for flying drones. For Example in the UK it’s Civil Aviation Authority (CAA) that restricts you from flying drones near airports or aircraft, keep the drone below 400 feet etc. Further you can refer to the [UK link](http://dronesafe.uk/drone-code/)

 * In the US it’s federal Aviation Administration (FAA) which has a code of not to fly above a group of people, never fly under influence of drugs and alcohol. Please refer to [here](https://www.faa.gov/uas/getting_started/fly_for_fun/)

 * Similarly, for various countries you have strict rules that need to be taken care of before making a decision of buying a drone. So, save yourself from getting disheartened of the fact that you cannot achieve the purpose for what you bought this drone. 

### Improve the drone flying skills

 A lot of people think that drones are hard to fly, but the truth is, they’re really not. Anyone capable of using an [iPhone](https://apps.apple.com/us/app/dronedeploy-flight-app/id971358101) or [Android](https://play.google.com/store/apps/details?id=com.dronedeploy.beta) device is more than capable of flying a drone. However, this does not mean that drones are fool proof. Even the most advanced drones require some general knowledge if you want to avoid crashing or worse, losing your drone forever. So you need to improve your flying drone skills.
 
### Where To Buy A Drone?

If you don’t know where to buy a drone, don’t worry. There are tons of online stores for drones that will ship to just about any major country. If you’re buying toy drones, the best place to go is Amazon or others below: 

 All of the main websites for buying drones.

  * **[dji.com](https://www.dji.com/)**: The #1 in popularity and name.

  * **[Amazon.com](https://www.amazon.com/drones/s?k=drones)**: A little bit of everything.

  * **[horizonhobby.com](https://www.horizonhobby.com/helicopters/drones/)**: The leader in radio control airplanes, cars, quads, radios and more.

  * **[amainhobbies.com](https://www.amainhobbies.com/drones/c3347)**: The great selection of RC Hobby.


## Geographic Information System

[Back to the Top](#table-of-contents)

[Geographic Information System (GIS)](https://www.usgs.gov/faqs/what-geographic-information-system-gis) is an information system able to encode, store, transform, analyze and display geospatial information.

 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/d0068592-b28a-4442-955e-bccd793a4625">
</br>
</p>

Image credit: [geo.university](https://www.geo.university/courses/environmental-modelling-and-analysis-in-gis)

### Geographic Information System Software

- [ArcGIS Desktop](https://www.esri.com/en-us/arcgis/products/arcgis-desktop/overview): Extendable desktop suite to manage, visualize and analyze GIS data in 2D and 3D, including image processing. Includes ArcGIS Pro, ArcMap, ArcCatalog, and ArcGIS Online.
- [DIVA-GIS](https://www.diva-gis.org/) - DIVA-GIS is a free geographic information system software program used for the analysis of geographic data, in particular point data on biodiversity.
- [GeoDa](http://geodacenter.github.io/) - A free and open source software tool that serves as an introduction to spatial data analysis.
- [GISInternals](http://www.gisinternals.com/) - Povidesdaily build packages and software development kits for the GDAL and MapServer
- [Global Mapper](http://www.bluemarblegeo.com/products/global-mapper.php) - An easy-to-use, robust, and genuinely affordable GIS application that combines a wide array of spatial data processing tools with access to an unparalleled variety of data formats.
- [GRASS GIS](https://grass.osgeo.org/) - A free and open source GIS software suite used for geospatial data management and analysis, image processing, graphics and maps production, spatial modeling, and visualization.
- [gvSIG](http://www.gvsig.com/en) - A powerful, user-friendly, interoperable GIS.
- [JUMP GIS](http://jump-pilot.sourceforge.net/) - An open source GIS written in Java
- [MapInfo Pro](https://www.pitneybowes.com/us/location-intelligence/geographic-information-systems/mapinfo-pro.html) - A full-featured desktop solution to prepare data for web mapping applications and create presentation quality maps that combines data analysis, visual insights, and map publishing.
- [Marble](https://marble.kde.org/) - A virtual globe and world atlas.
- [OpenOrienteering Mapper](https://github.com/openorienteering/mapper) - A software for creating maps for the orienteering sport.
- [QGIS](http://qgis.org/en/site/) - A free and open source GIS.
- [SAGA](http://www.saga-gis.org/en/index.html) - Open source system for automated geoscientific analyses.
- [SharpMap](https://github.com/SharpMap/SharpMap) - An easy-to-use mapping library for use in web and desktop applications
- [TileMill](https://tilemill-project.github.io/tilemill/) - An open source map design studio, developed by a community of volunteer open source contributors
- [Whitebox GAT](http://www.uoguelph.ca/~hydrogeo/Whitebox/) - An open source desktop GIS and remote sensing software package for general applications of geospatial analysis and data visualization.
- [DIVA-GIS](https://www.diva-gis.org/) - DIVA-GIS is a free geographic information system software program used for the analysis of geographic data, in particular point data on biodiversity.
- [Abc-Map](https://abc-map.fr/) - A lightweight and user-friendly Web GIS. Create, import data from various sources, export maps or share them online freely and easily.


## Remote Sensing

[Back to the Top](#table-of-contents)

[Remote Sensing](https://www.earthdata.nasa.gov/learn/backgrounders/remote-sensing) is a set of  techniques used to gather and process information about an object without direct physical contact.

 * **Active remote sensing** are instruments that operate with their own source of emission or light, while passive ones rely on the reflected one. Radiation also differs by wavelengths that fall into short (visible, NIR, MIR) and long (microwave). Active remote sensing techniques differ by what they transmit (light or waves) and what they determine (distance, height, atmospheric conditions, etc.).

 * **Passive remote sensing** are instruments that depend on natural energy (sunrays) bounced by the target. For this reason, it can be applied only with proper sunlight, otherwise there will be nothing to reflect. It employs multispectral or hyperspectral sensors that measure the acquired quantity with multiple band combinations. These combinations differ by the number of channels (two wavelengths and more). The scope of bands (visible, IR, NIR, TIR, microwave).

<p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/b7aabdc2-5f15-4b3a-9caf-1d3368105086)">
</br>
</p>

Image credit: [mdpi](https://www.mdpi.com/2072-4292/12/18/3053)

### Remote Sensing Software
- [eCognition](http://www.ecognition.com/suite/ecognition-developer) - A powerful development environment for object-based image analysis.
- [ENVI](https://www.harris.com/solution/envi) :star2: - A geospatial imagery analysis and processing software.
- [ERDAS IMAGINE](https://www.hexagongeospatial.com/products/power-portfolio/erdas-imagine) :star2: - A geospatial imagery analysis and processing software.
- [Google Earth](https://www.google.com/earth/) - A computer program that renders a 3D representation of Earth based on satellite imagery.
- [Google Earth Studio](https://www.google.com/earth/studio/) - An animation tool for Google Earth’s satellite and 3D imagery.
- [GRASS GIS](https://grass.osgeo.org/) - A free and open source GIS software suite used for geospatial data management and analysis, image processing, graphics and maps production, spatial modeling, and visualization.
- [Opticks](https://opticks.org/) - An expandable remote sensing and imagery analysis software platform that is free and open source.
- [Orfeo toolbox](https://www.orfeo-toolbox.org/) - An open-source project for state-of-the-art remote sensing, including a fast image viewer, apps callable from Bash, Python or QGIS, and a powerful C++ API.
- [PANOPLY](https://www.giss.nasa.gov/tools/panoply/)- Panoply plots geo-referenced and other arrays from netCDF, HDF, GRIB, and other datasets.
- [PCI Geomatica](http://www.pcigeomatics.com/software/geomatica/professional) - A remote sensing desktop software package for processing earth observation data.
- [SNAP](http://step.esa.int/main/toolboxes/snap/) - A common architecture for all Sentinel Toolboxes.


## Point Cloud Processing

[Back to the Top](#table-of-contents)

[Point Cloud Processing](https://www.mathworks.com/discovery/point-cloud.html) is a huge number of tiny data points that exist in three dimensions(3D). If you could spit those points out of a scanner they would appear as a cloud. This can be used for mapping, perception, and navigation in robotics and autonomous systems. It can also be used in augmented reality (AR) and virtual reality (VR) applications.

**Functions of point cloud processing software include:**

  - Manual editing of the point cloud.
  - Automatic cleanup and filtering.
  - Offloading tasks to the cloud.
  - Rendering.
  - Point distance calculation.
  - Registration.
  - Conversion to mesh.
  - Conversation to [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline).
  
 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/eb6ace00-39c5-4a4b-b482-424faa208a74">
  <br />
</p>

Point Cloud Processing & Data Management. Image credit: [H2H Associates](http://h2hassociates.com/services/point-cloud-processing-data-management/)

### Point Cloud Processing Software 

- [**CloudCompare**](https://www.cloudcompare.org/) is a 3D point cloud processing software. It can also handle triangular meshes and calibrated images. 
- [**PCL - Point Cloud Library**](https://pointclouds.org/) is a standalone, large scale, open project for 2D/3D image and point cloud processing.
- [**Leica Cyclone**](https://leica-geosystems.com/products/laser-scanners/software/leica-cyclone?redir=w226) is the market-leading point cloud processing software. It is a family of software modules that provides the widest set of work process options for 3D laser scanning projects in engineering, surveying, construction and related applications. 
- [**FARO SCENE**](https://www.faro.com/en/Products/Software/SCENE-Software) is a software that allows you to capture, process and register real-world objects and environments in 3D point cloud. You can create stunning visualizations, share and collaborate, and access virtual reality -LRB- VR -RRB- views of your scans.
- [**Autodesk ReCap**](https://www.autodesk.com/support/technical/product/recap) is a software that let's you create accurate 3D models with reality capture using laser scanning. This software, which lets you convert reality into a 3D model or 2D drawing, actually comes in two flavors: ReCap and ReCap Pro. 
- [**Trimble RealWorks**](https://geospatial.trimble.com/en/products/software/trimble-realworks) is a powerful office software suite to integrate 3D point cloud and survey data. It effectively manages large scan datasets to register, analyze, model, collaborate and produce compelling deliverables. 
- [**PDAL - Point Data Abstraction Library**](http://www.pdal.io/) is a C++/Python BSD library for translating and manipulating point cloud data.
- [**libLAS**](http://liblas.org/) is a C/C++ library for reading and writing the very common LAS LiDAR format (Legacy. Replaced by PDAL).
- [**entwine**](https://github.com/connormanning/entwine/) is a data organization library for massive point clouds, designed to conquer datasets of hundreds of billions of points as well as desktop-scale point clouds.
- [**PotreeConverter**](https://github.com/potree/PotreeConverter) is another data organisation library, generating data for use in the Potree web viewer.
- [**lidR**](https://github.com/Jean-Romain/lidR) is a R package for Airborne LiDAR Data Manipulation and Visualization for Forestry Applications. 
- [**pypcd**](https://github.com/dimatura/pypcd) is a Python module to read and write point clouds stored in the PCD file format, used by the Point Cloud Library.
- [**Open3D**](https://github.com/intel-isl/Open3D) is an open-source library that supports rapid development of software that deals with 3D data. It has Python and C++ frontends.
- [**cilantro**](https://github.com/kzampog/cilantro) is a Lean and Efficient Library for Point Cloud Data Processing (C++).
- [**PyVista**](https://github.com/pyvista/pyvista/) is a 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit(VTK).
- [**pyntcloud**](https://github.com/daavoo/pyntcloud) is a Python library for working with 3D point clouds.
- [**pylas**](https://github.com/tmontaigu/pylas) Reading Las (lidar) in Python.
- [**PyTorch**](https://github.com/rusty1s/pytorch_geometric) PyTorch Geometric (PyG) is a geometric deep learning extension library for PyTorch.
- [**Paraview**](http://www.paraview.org/) is a Open-source, multi-platform data analysis and visualization application. 
- [**MeshLab**](http://meshlab.sourceforge.net/) is a Open source, portable, and extensible system for the processing and editing of unstructured 3D triangular meshes
- [**OpenFlipper**](http://www.openflipper.org/) is a Open Source Geometry Processing and Rendering Framework.
- [**PotreeDesktop**](https://github.com/potree/PotreeDesktop) is a desktop/portable version of the web-based point cloud viewer [**Potree**](https://github.com/potree/potree)
- [**3d-annotation-tool**](https://github.com/StrayRobots/3d-annotation-tool) is a lightweight desktop application to annotate pointclouds for machine learning.

## LiDAR

[Back to the Top](#table-of-contents)
   
[Light Detection and Ranging (LiDAR)](https://www.usgs.gov/news/earthword-lidar) is a technology used to create high-resolution models of ground elevation with a vertical accuracy of 10 centimeters (4 inches). Lidar equipment, which includes a laser scanner, a Global Positioning System (GPS), and an Inertial Navigation System (INS), is typically mounted on a small aircraft. The laser scanner transmits brief pulses of light to the ground surface. Those pulses are reflected or scattered back and their travel time is used to calculate the distance between the laser scanner and the ground.  Lidar data is initially collected as a “point cloud” of individual points reflected from everything on the surface, including structures and vegetation. To produce a “bare earth” Digital Elevation Model (DEM), structures and vegetation are stripped away.

 <p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950840-fe9efa80-cd0e-11eb-9a12-57c4799d63b5.png">
  <br />
</p>

**3D Data Visualization of Golden Gate Bridge. Source: [USGS](https://www.usgs.gov/core-science-systems/ngp/tnm-delivery)**

[Mola](https://docs.mola-slam.org/latest/) is a Modular Optimization framework for Localization and mApping (MOLA).

 <p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950850-01015480-cd0f-11eb-9fa6-1f93d6d87cd1.gif">
  <br />
</p>

**3D LiDAR SLAM from KITTI dataset. Source: [MOLA](https://docs.mola-slam.org/latest/demo-kitti-lidar-slam.html)**


 ### Basic matching algorithms
- [Iterative closest point (ICP) ](https://www.youtube.com/watch?v=uzOCS_gdZuM) - The must-have algorithm for feature matching applications (ICP).
  - [GitHub repository](https://github.com/pglira/simpleICP) - simpleICP C++ /Julia / Matlab / Octave / Python implementation.
  - [GitHub repository](https://github.com/ethz-asl/libpointmatcher) - libpointmatcher, a modular library implementing the ICP algorithm.

- [Normal distributions transform](https://www.youtube.com/watch?v=0YV4a2asb8Y) - More recent massively-parallel approach to feature matching (NDT).
- [KISS-ICP](https://www.youtube.com/watch?v=kMMH8rA1ggI) - In Defense of Point-to-Point ICP – Simple, Accurate, and Robust Registration If Done the Right Way.
  - [GitHub repository](https://github.com/PRBonn/kiss-icp)
  

### Semantic segmentation
- [RangeNet++](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/milioto2019iros.pdf) - Fast and Accurate LiDAR Sematnic Segmentation with fully convolutional network.
  - [GitHub repository](https://github.com/PRBonn/rangenet_lib)
  - [YouTube video](https://www.youtube.com/watch?v=uo3ZuLuFAzk)
- [PolarNet](https://arxiv.org/pdf/2003.14032.pdf) - An Improved Grid Representation for Online LiDAR Point Clouds Semantic Segmentation.
  - [GitHub repository](https://github.com/edwardzhou130/PolarSeg)
  - [YouTube video](https://www.youtube.com/watch?v=iIhttRSMqjE)
- [Frustum PointNets](https://arxiv.org/pdf/1711.08488.pdf) - Frustum PointNets for 3D Object Detection from RGB-D Data.
  - [GitHub repository](https://github.com/charlesq34/frustum-pointnets)
- [Study of LIDAR Semantic Segmentation](https://larissa.triess.eu/scan-semseg/) - Scan-based Semantic Segmentation of LiDAR Point Clouds: An Experimental Study IV 2020.
  - [Paper](https://arxiv.org/abs/2004.11803)
  - [GitHub repository](http://ltriess.github.io/scan-semseg)
- [LIDAR-MOS](https://www.ipb.uni-bonn.de/pdfs/chen2021ral-iros.pdf) - Moving Object Segmentation in 3D LIDAR Data
  - [GitHub repository](https://github.com/PRBonn/LiDAR-MOS)
  - [YouTube video](https://www.youtube.com/watch?v=NHvsYhk4dhw)
- [SuperPoint Graph](https://arxiv.org/pdf/1711.09869.pdf)- Large-scale Point Cloud Semantic Segmentation with Superpoint Graphs
  - [GitHub repository](https://github.com/PRBonn/LiDAR-MOS)
  - [YouTube video](https://www.youtube.com/watch?v=Ijr3kGSU_tU)
- [RandLA-Net](https://arxiv.org/pdf/1911.11236.pdf) - Efficient Semantic Segmentation of Large-Scale Point Clouds
  - [GitHub repository](https://github.com/QingyongHu/RandLA-Net)
  - [YouTube video](https://www.youtube.com/watch?v=Ar3eY_lwzMk)
- [Automatic labelling](https://arxiv.org/pdf/2108.13757.pdf) - Automatic labelling of urban point clouds using data fusion
  - [GitHub repository](https://github.com/Amsterdam-AI-Team/Urban_PointCloud_Processing)
  - [YouTube video](https://www.youtube.com/watch?v=qMj_WM6D0vI)

### Ground segmentation
- [Plane Seg](https://github.com/ori-drs/plane_seg) - ROS comapatible ground plane segmentation; a library for fitting planes to LIDAR.
  - [YouTube video](https://www.youtube.com/watch?v=YYs4lJ9t-Xo)
- [LineFit Graph](https://ieeexplore.ieee.org/abstract/document/5548059)- Line fitting-based fast ground segmentation for horizontal 3D LiDAR data
  - [GitHub repository](https://github.com/lorenwel/linefit_ground_segmentation)
- [Patchwork](https://arxiv.org/pdf/2108.05560.pdf)- Region-wise plane fitting-based robust and fast ground segmentation for 3D LiDAR data 
  - [GitHub repository](https://github.com/LimHyungTae/patchwork)
  - [YouTube video](https://www.youtube.com/watch?v=rclqeDi4gow)
- [Patchwork++](https://arxiv.org/pdf/2207.11919.pdf)- Improved version of Patchwork. Patchwork++ provides pybinding as well for deep learning users
  - [GitHub repository](https://github.com/url-kaist/patchwork-plusplus-ros)
  - [YouTube video](https://www.youtube.com/watch?v=fogCM159GRk)


### Simultaneous localization and mapping SLAM and LIDAR-based odometry and or mapping LOAM
- [LOAM J. Zhang and S. Singh](https://youtu.be/8ezyhTAEyHs) - LOAM: Lidar Odometry and Mapping in Real-time.
- [LeGO-LOAM](https://github.com/RobustFieldAutonomyLab/LeGO-LOAM) - A lightweight and ground optimized lidar odometry and mapping (LeGO-LOAM) system for ROS compatible UGVs. 
  - [YouTube video](https://www.youtube.com/watch?v=7uCxLUs9fwQ)
- [Cartographer](https://github.com/cartographer-project/cartographer) - Cartographer is ROS compatible system that provides real-time simultaneous localization and mapping (SLAM) in 2D and 3D across multiple platforms and sensor configurations.
  - [YouTube video](https://www.youtube.com/watch?v=29Knm-phAyI)
- [SuMa++](http://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/chen2019iros.pdf) - LiDAR-based Semantic SLAM.
  - [GitHub repository](https://github.com/PRBonn/semantic_suma/)
  - [YouTube video](https://youtu.be/uo3ZuLuFAzk)
- [OverlapNet](http://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/chen2020rss.pdf) -  Loop Closing for LiDAR-based SLAM.
  - [GitHub repository](https://github.com/PRBonn/OverlapNet)
  - [YouTube video](https://www.youtube.com/watch?v=YTfliBco6aw)
- [LIO-SAM](https://arxiv.org/pdf/2007.00258.pdf) - Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping.
  - [GitHub repository](https://github.com/TixiaoShan/LIO-SAM)
  - [YouTube video](https://www.youtube.com/watch?v=A0H8CoORZJU)
- [Removert](http://ras.papercept.net/images/temp/IROS/files/0855.pdf) - Remove, then Revert: Static Point cloud Map Construction using Multiresolution Range Images.
  - [GitHub repository](https://github.com/irapkaist/removert)
  - [YouTube video](https://www.youtube.com/watch?v=M9PEGi5fAq8)

### Object detection and object tracking
- [Learning to Optimally Segment Point Clouds](https://arxiv.org/abs/1912.04976) - By Peiyun Hu, David Held, and Deva Ramanan at Carnegie Mellon University. IEEE Robotics and Automation Letters, 2020.
  - [YouTube video](https://www.youtube.com/watch?v=wLxIAwIL870)
  - [GitHub repository](https://github.com/peiyunh/opcseg)
- [Leveraging Heteroscedastic Aleatoric Uncertainties for Robust Real-Time LiDAR 3D Object Detection](https://arxiv.org/pdf/1809.05590.pdf) - By Di Feng, Lars Rosenbaum, Fabian Timm, Klaus Dietmayer. 30th IEEE Intelligent Vehicles Symposium, 2019.
  - [YouTube video](https://www.youtube.com/watch?v=2DzH9COLpkU)
- [What You See is What You Get: Exploiting Visibility for 3D Object Detection](https://arxiv.org/pdf/1912.04986.pdf) - By Peiyun Hu, Jason Ziglar, David Held, Deva Ramanan, 2019.
  - [YouTube video](https://www.youtube.com/watch?v=497OF-otY2k)
  - [GitHub repository](https://github.com/peiyunh/WYSIWYG)
- [urban_road_filter](https://doi.org/10.3390/s22010194)-
Real-Time LIDAR-Based Urban Road and Sidewalk Detection for Autonomous Vehicles
  - [GitHub repository](https://github.com/jkk-research/urban_road_filter)
  - [YouTube video](https://www.youtube.com/watch?v=T2qi4pldR-E)

  
## Neural Radiance Field (NeRF)

[Back to the Top](#table-of-contents)

[NeRF (Neural Radiance Field)](https://developer.nvidia.com/blog/getting-started-with-nvidia-instant-nerfs/) is a neural rendering model that learns a high-resolution 3D scene in seconds and can render images of that scene in a few milliseconds. It works by taking a handful a of 2D images representing a scene and [interpolating](https://en.wikipedia.org/wiki/Interpolation) between them to render one complete 3D scene.
 
 * [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](http://tancik.com/nerf)
 * [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding (PDF)](https://nvlabs.github.io/instant-ngp/assets/mueller2022instant.pdf)
 * [Instant Neural Graphics Primitives](https://github.com/NVlabs/instant-ngp)
 * [Neural Radiance Field (NeRF): A Gentle Introduction ](https://datagen.tech/guides/synthetic-data/neural-radiance-field-nerf/)
 
 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/2e37a94b-a92b-489f-843d-a43afc5dbc13">
</br>
</p>

NVIDIA Instant NeRFs. Image Credit: [NVIDIA](https://developer.nvidia.com/blog/getting-started-with-nvidia-instant-nerfs/)

[Tiny CUDA Neural Networks](https://github.com/NVlabs/tiny-cuda-nn) is a small, self-contained framework for training and querying neural networks. Most notably, it contains a lightning fast ["fully fused" multi-layer perceptron](https://raw.githubusercontent.com/NVlabs/tiny-cuda-nn/master/data/readme/fully-fused-mlp-diagram.png) ([technical paper](https://tom94.net/data/publications/mueller21realtime/mueller21realtime.pdf)), a versatile [multiresolution hash encoding](https://raw.githubusercontent.com/NVlabs/tiny-cuda-nn/master/data/readme/multiresolution-hash-encoding-diagram.png) ([technical paper](https://nvlabs.github.io/instant-ngp/assets/mueller2022instant.pdf)), as well as support for various other input encodings, losses, and optimizers.

 <p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/c92637b1-5e96-44b1-a715-97b6eecab641">
</br>
</p>

NVIDIA Instant NeRFs using tiny-cuda-nn (Tiny CUDA Neural Networks). Image Credit: [NVIDIA](https://github.com/NVlabs/instant-ngp/blob/master/docs/assets_readme/testbed.png)

<details open>
<summary>Compression</summary>

- [Variable Bitrate Neural Fields](https://nv-tlabs.github.io/vqad/), Takikawa et al., SIGGRAPH 2022 | [github](https://github.com/nv-tlabs/vqad)
</details>

<details open>
<summary>Unconstrained Images</summary>

- [NeRF in the Wild: Neural Radiance Fields for Unconstrained Photo Collections](https://nerf-w.github.io/), Martin-Brualla et al., CVPR 2021 <!---MartinBrualla20arxiv_nerfw-->
- [Ha-NeRF: Hallucinated Neural Radiance Fields in the Wild](https://rover-xingyu.github.io/Ha-NeRF/), Chen et al., CVPR 2022 | [github](https://github.com/rover-xingyu/Ha-NeRF) <!---chen2021hallucinated-->
- [HDR-Plenoxels: Self-Calibrating High Dynamic Range Radiance Fields](https://hdr-plenoxels.github.io/), Jun-seong et al., ECCV 2022 | [github](https://github.com/postech-ami/HDR-Plenoxels) <!---Jun-seong2022hdr-plenoxels-->
</details>

<details open>
<summary>Pose Estimation</summary>

- [iNeRF: Inverting Neural Radiance Fields for Pose Estimation](http://yenchenlin.me/inerf/), Yen-Chen et al. IROS 2021 <!---YenChen20arxiv_iNeRF-->
- [A-NeRF: Surface-free Human 3D Pose Refinement via Neural Rendering](https://zollhoefer.com/papers/arXiv20_ANeRF/page.html), Su et al. Arxiv 2021 <!---Su21arxiv_A_NeRF-->
- [NeRF--: Neural Radiance Fields Without Known Camera Parameters](http://nerfmm.active.vision/), Wang et al., Arxiv 2021 | [github](https://github.com/ActiveVisionLab/nerfmm) <!---Wang21arxiv_nerfmm-->
- [iMAP: Implicit Mapping and Positioning in Real-Time](https://edgarsucar.github.io/iMAP/), Sucar et al., ICCV 2021
- [NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://pengsongyou.github.io/nice-slam), Zhu et al., Arxiv 2021
- [GNeRF: GAN-based Neural Radiance Field without Posed Camera](https://arxiv.org/abs/2103.15606), Meng et al., Arxiv 2021
- [BARF: Bundle-Adjusting Neural Radiance Fields](https://chenhsuanlin.bitbucket.io/bundle-adjusting-NeRF/), Lin et al., ICCV 2021 
- [Self-Calibrating Neural Radiance Fields](https://postech-cvlab.github.io/SCNeRF/), Jeong et al., ICCV 2021 | [github](https://github.com/POSTECH-CVLab/SCNeRF)
- [L2G-NeRF: Local-to-Global Registration for Bundle-Adjusting Neural Radiance Fields](https://rover-xingyu.github.io/L2G-NeRF/), Chen et al., CVPR 2023 | [github](https://github.com/rover-xingyu/L2G-NeRF)
- [Loc-NeRF: Monte Carlo Localization using Neural Radiance Fields](https://arxiv.org/abs/2209.09050), Maggio et al., ICRA 2023 | [github](https://github.com/MIT-SPARK/Loc-NeRF)
- [Robust Camera Pose Refinement for Multi-Resolution Hash Encoding](http://arxiv.org/abs/2302.01571), Heo et al., ICML 2023.
</details>

<details open>
<summary>Compositionality</summary>

- [NeRF++: Analyzing and Improving Neural Radiance Fields](https://arxiv.org/abs/2010.07492), Zhang et al., Arxiv 2020 | [github](https://github.com/Kai-46/nerfplusplus) <!---Zhang20arxiv_nerf++-->
- [GIRAFFE: Representing Scenes as Compositional Generative Neural Feature Fields](https://arxiv.org/abs/2011.12100), Niemeyer et al., CVPR 2021. <!---Niemeyer20arxiv_GIRAFFE-->
- [Object-Centric Neural Scene Rendering](https://shellguo.com/osf/), Guo et al., Arxiv 2020 <!---Guo20arxiv_OSF-->
- [Learning Compositional Radiance Fields of Dynamic Human Heads](https://ziyanw1.github.io/hybrid_nerf/), Wang et al., Arxiv 2020. <!---Wang20arxiv_hybrid_NeRF-->
- [Neural Scene Graphs for Dynamic Scenes](https://light.princeton.edu/neural-scene-graphs/), Ost et al., CVPR 2021. <!---Ost20arxiv_NeuralSceneGraphs-->
- [Unsupervised Discovery of Object Radiance Fields](https://kovenyu.com/uorf/), Yu et al., Arxiv 2021 .
- [Learning Object-Compositional Neural Radiance Field for Editable Scene Rendering](https://zju3dv.github.io/object_nerf/), Yang et al., ICCV 2021 | [github](https://github.com/zju3dv/object_nerf) <!---yang2021objectnerf-->
- [MoFaNeRF: Morphable Facial Neural Radiance Field](https://neverstopzyy.github.io/mofanerf/), Zhuang et al., Arxiv 2021 | [github](https://github.com/zhuhao-nju/mofanerf)
</details>

<details open>
<summary>Scene Labelling and Understanding</summary>

- [In-Place Scene Labelling and Understanding with Implicit Scene Representation](https://shuaifengzhi.com/Semantic-NeRF/), Zhi et al., Arxiv 2021.
- [NeRF-SOS: Any-view Self-supervised Object Segmentation on Complex Real-world Scenes](https://zhiwenfan.github.io/NeRF-SOS/), Fan et al., ICLR 2023.
</details>

<details open>
<summary>Object Category Modeling</summary>

- [FiG-NeRF: Figure Ground Neural Radiance Fields for 3D Object Category Modelling](https://fig-nerf.github.io/), Xie et al., Arxiv 2021.
- [NeRF-Tex: Neural Reflectance Field Textures](https://developer.nvidia.com/blog/nvidia-research-nerf-tex-neural-reflectance-field-textures/), Baatz et al., EGSR 2021.
</details>

<details open>
<summary>Multi-scale</summary>

- [Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields](https://jonbarron.info/mipnerf/), Barron et al., Arxiv 2021 | [github](https://github.com/google/mipnerf)
- [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](https://jonbarron.info/mipnerf360/), Barron et al., Arxiv 2022.
</details>

<details open>
<summary>Model Reconstruction</summary>

- [UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction](https://arxiv.org/abs/2104.10078), Oechsle et al., ICCV 2021
- [NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction](https://arxiv.org/abs/2106.10689), Wang et al., NeurIPS 2021 | [github](https://github.com/Totoro97/NeuS)
- [Volume Rendering of Neural Implicit Surfaces](https://arxiv.org/abs/2106.12052), Yariv et al., NeurIPS 2021 | [github](https://github.com/ventusff/neurecon)
- [NeAT: Learning Neural Implicit Surfaces with Arbitrary Topologies from Multi-view Images](https://arxiv.org/abs/2303.12012), Meng et al., CVPR 2023 | [github](https://github.com/xmeng525/NeAT)
</details>


<details open>
<summary>Depth Estimation</summary>

- [NerfingMVS: Guided Optimization of Neural Radiance Fields for Indoor Multi-view Stereo](https://weiyithu.github.io/NerfingMVS/), Wei et al., ICCV 2021.
</details>


<details open>
<summary>Robotics</summary>

- [3D Neural Scene Representations for Visuomotor Control](https://3d-representation-learning.github.io/nerf-dy/), Li et al., CoRL 2021 Oral.
- [Vision-Only Robot Navigation in a Neural Radiance World](https://arxiv.org/abs/2110.00168), Adamkiewicz et al., RA-L 2022 Vol.7 No.2 .
</details>

<details open>
<summary>Large-scale scene</summary>

- [Switch-NeRF: Learning Scene Decomposition with Mixture of Experts for Large-scale Neural Radiance Fields](https://mizhenxing.github.io/switchnerf), Mi et al., ICLR 2023 | [github](https://github.com/MiZhenxing/Switch-NeRF)
</details>

## LERF(Language Embedded Radiance Fields)

[Back to the Top](#table-of-contents)

[LERF(Language Embedded Radiance Fields)](https://www.lerf.io/) is a AI process that optimizes a dense, multi-scale language 3D field by volume rendering CLIP embeddings along training rays, supervising these embeddings with multi-scale CLIP features across multi-view training images. 

<p align="center">
 <img src="https://github.com/mikeroyal/Photogrammetry-Guide/assets/45159366/c6c9e849-32cf-4b0a-9e37-de2335e6659f">
</br>
</p>

LERF Rendering. Image credit: [LERF.io](https://www.lerf.io/)


### Certifications & Courses
[Back to the Top](#table-of-contents)

 - [ASPRS (American Society for Photogrammetry and Remote Sensing) Certification Program](https://www.asprs.org/certification)

 - [Pix4D training and certification for mapping professionals](https://training.pix4d.com/)

 - [Drone mapping and photogrammetry workshops with Pix4D](https://training.pix4d.com/pages/workshops)
 
 - [Top Photogrammetry Courses Online | Udemy](https://www.udemy.com/topic/photogrammetry/)

 - [Photogrammetry With Drones: In Mapping Technology | Udemy](https://www.udemy.com/course/essentials-of-photogrammetry/)

 - [Introduction to Photogrammetry Course | Coursera](https://www.coursera.org/lecture/aerial-photography-with-uav/introduction-to-photogrammetry-KyP30)

 - [Photogrammetry Online Classes and Training | Linkedin Learning](https://www.linkedin.com/learning/search?keywords=Photogrammetry&upsellOrderOrigin=default_guest_learning&trk=learning-course_learning-search-bar_search-submit)

 - [Digital Photogrammetric Systems Course | Purdue Online Learning](https://engineering.purdue.edu/online/courses/digital-photogrammetric-systems)

 - [Photogrammetry Training | Deep3D Photogrammetry](https://deep3d.co.uk/photogrammetry-training/)
 
 - [Blender 3 + Reality Capture 5hr. Tutorial Course, with Futuristic Movie Scene & Files](https://blendermarket.com/products/blender-3--reality-capture-cinematic-render-course-futuristic-movie-film-scene)
  
 - [Photogrammetry Course: Photoreal 3d With Blender And Reality Capture](https://blendermarket.com/products/photogrammetry-course)
 
 - [Advanced PhotoModeler for Collision Reconstruction | LightPoint Course](https://lightpointdata.com/advanced-photogrammetry)
 
 - [Motorcycle Collision Reconstruction | LightPoint Course](https://lightpointdata.com/motorcycle-collision-reconstruction)
 
 - [Point Clouds in Collision Reconstruction | LightPoint Course](https://lightpointdata.com/point-clouds-in-collision-reconstruction-future)
 
 - [Advanced Photogrammetry and Mapping with UAS Certificate | Michigan Tech Unviserity](https://www.mtu.edu/gradschool/programs/certificates/photogrammetry-mapping/)
 
 - [Cesium Certified Developer Program](https://cesium.com/learn/certifications/)

### Books/eBooks
[Back to the Top](#table-of-contents)

- [73 Best Photogrammetry Books of All Time - BookAuthority](https://bookauthority.org/books/best-photogrammetry-books)

- [Photogrammetry E-books/tutorials | GIS Resources](https://gisresources.com/photogrammetry-e-books/)

- [Create photorealistic game assets with Unity Engine(eBook)](https://unity.com/solutions/photogrammetry)

- [Get ready for Photogrammetry: A beginner’s guide to scan clean-up with Unity ArtEngine (PDF)](https://content.cdntwrk.com/files/aT0xNDQ5MzA2JnY9MSZpc3N1ZU5hbWU9Z2V0LXJlYWR5LWZvci1waG90b2dyYW1tZXRyeSZjbWQ9ZCZzaWc9ZWZmOGJkNjJlOTA1Yzc2ZGFmMTc3MjVmODMzNDBjNTc%253D)

- [Introduction to Modern Photogrammetry by MIKHAIL EDWARD](https://www.amazon.com/Introduction-Modern-Photogrammetry-Edward-Mikhail/dp/8126539984/ref=sr_1_5?crid=2ZTDXM9NZX73K&keywords=Photogrammetry&qid=1654415794&s=books&sprefix=photogrammetry%2Cstripbooks%2C157&sr=1-5)

 - [UAV Photogrammetry and Remote Sensing by Fernando Carvajal-Ramírez, Francisco Agüera-Vega](https://www.amazon.com/Photogrammetry-Remote-Sensing-Fernando-Carvajal-Ram%C3%ADrez/dp/3036514546/ref=sr_1_4?crid=2ZTDXM9NZX73K&keywords=Photogrammetry&qid=1654415794&s=books&sprefix=photogrammetry%2Cstripbooks%2C157&sr=1-4)
 
 - [Elements of Photogrammetry with Application in GIS, Fourth Editionby Paul Wolf, Bon DeWitt](https://www.amazon.com/Elements-Photogrammetry-Application-GIS-Fourth/dp/0071761128/ref=sr_1_2?crid=2ZTDXM9NZX73K&keywords=Photogrammetry&qid=1654415794&s=books&sprefix=photogrammetry%2Cstripbooks%2C157&sr=1-2)
 
 - [OpenDroneMap: The Missing Guide: A Practical Guide To Drone Mapping Using Free and Open Source Software
by Piero Toffanin](https://www.amazon.com/OpenDroneMap-Missing-Practical-Mapping-Software/dp/1086027566/ref=sr_1_16?crid=2ZTDXM9NZX73K&keywords=Photogrammetry&qid=1654415923&refinements=p_72%3A1250221011&rnid=1250219011&s=books&sprefix=photogrammetry%2Cstripbooks%2C157&sr=1-16)

 - [Digital Photogrammetry by Yves Egels and Michel Kasser](https://www.amazon.com/Michel-Kasser/e/B001H6L0CS?ref=sr_ntt_srch_lnk_19&qid=1654415923&sr=1-19)
 
 - [Digital Photogrammetry: Theory and Applications by Wilfried Linder ](https://www.amazon.com/Digital-Photogrammetry-Applications-Wilfried-Linder-ebook/dp/B00FBVV9VM/ref=sr_1_22?crid=2ZTDXM9NZX73K&keywords=Photogrammetry&qid=1654415923&refinements=p_72%3A1250221011&rnid=1250219011&s=books&sprefix=photogrammetry%2Cstripbooks%2C157&sr=1-22)
 
 - [Drone Technology in Architecture, Engineering and Construction: A Strategic Guide to Unmanned Aerial Vehicle Operation and Implementation by Daniel Tal and Jon Altschuld ](https://www.amazon.com/Drone-Technology-Architecture-Engineering-Construction/dp/1119545889/ref=sr_1_35?crid=2ZTDXM9NZX73K&keywords=Photogrammetry&qid=1654416094&refinements=p_72%3A1250221011&rnid=1250219011&s=books&sprefix=photogrammetry%2Cstripbooks%2C157&sr=1-35)
 
  - [Getting to Know ArcGIS Desktop 10.8 by Michael Law and Amy Collins](https://www.amazon.com/Getting-Know-ArcGIS-Desktop-10-8/dp/1589485777/ref=sr_1_2?keywords=Getting+to+Know+ArcGIS&qid=1659566233&sr=8-2)
 
 - [Getting to Know ArcGIS Pro 2.8 by Michael Law and Amy Collins](https://www.amazon.com/Getting-Know-ArcGIS-Pro-2-8/dp/158948701X/ref=sr_1_5?keywords=Getting+to+Know+ArcGIS&qid=1659566233&sr=8-5)
 
 - [Getting to Know Web GIS by Pinde Fu](https://www.amazon.com/Getting-Know-Web-GIS-Pinde-ebook/dp/B09Y68TXGF/ref=sr_1_3?crid=303PWBITFO5JT&keywords=web+GIS&qid=1659566920&sprefix=web+gis%2Caps%2C200&sr=8-3)
 
 - [Geographical Data Science and Spatial Data Analysis: An Introduction in R (Spatial Analytics and GIS) by Lex Comber and Chris Brunsdon](https://www.amazon.com/Geographical-Data-Science-Spatial-Analysis/dp/1526449366/ref=sr_1_3?crid=38CZ6KLAF9GQ0&keywords=An+Introduction+to+R+for+Spatial+Analysis+and+Mapping&qid=1659566504&sprefix=an+introduction+to+r+for+spatial+analysis+and+mapping%2Caps%2C152&sr=8-3)
 
 - [Fuzzy Machine Learning Algorithms for Remote Sensing Image Classification by Anil Kumar , Priyadarshi Upadhyay, et al.](https://www.amazon.com/Machine-Learning-Algorithms-Sensing-Classification-ebook/dp/B08C27QSSW/ref=sr_1_fkmr0_2?crid=O5TAKPDUTE86&keywords=Imagery+and+GIS%3A+Best+Practices+for+Extracting+Information+from+Imagery&qid=1659566587&sprefix=imagery+and+gis+best+practices+for+extracting+information+from+imagery%2Caps%2C159&sr=8-2-fkmr0)
 
 - [GIS Applications in Agriculture, Volume Four by Tom Mueller, Gretchen F. Sassenrath](https://www.amazon.com/GIS-Applications-Agriculture-Four-Mueller/dp/1032098805/ref=sr_1_fkmr1_1?crid=O5TAKPDUTE86&keywords=Imagery+and+GIS%3A+Best+Practices+for+Extracting+Information+from+Imagery&qid=1659566587&sprefix=imagery+and+gis+best+practices+for+extracting+information+from+imagery%2Caps%2C159&sr=8-1-fkmr1)
 
 - [Applications of Small Unmanned Aircraft Systems: Best Practices and Case Studies by J.B. Sharma](https://www.amazon.com/Applications-Small-Unmanned-Aircraft-Systems/dp/0367199246/ref=sr_1_fkmr1_2?crid=O5TAKPDUTE86&keywords=Imagery+and+GIS%3A+Best+Practices+for+Extracting+Information+from+Imagery&qid=1659566587&sprefix=imagery+and+gis+best+practices+for+extracting+information+from+imagery%2Caps%2C159&sr=8-2-fkmr1)
 
 - [Free GIS Books](https://www.gislounge.com/free-gis-books/)

### YouTube Tutorials
[Back to the Top](#table-of-contents)

 [![Introduction to Photogrammetry (Cyrill Stachniss, 2021](https://ytcards.demolab.com/?id=SyB7Wg1e62A&list=RDCMUCi1TC2fLRvgBQNe-T4dp8Eg&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Introduction to Photogrammetry (Cyrill Stachniss, 2021")](https://www.youtube.com/watch?v=SyB7Wg1e62A&list=RDCMUCi1TC2fLRvgBQNe-T4dp8Eg) 
 [![Complete Meshroom Tutorial | Photogrammetry Course by Gleb Alexandrov](https://ytcards.demolab.com/?id=j3lhPKF8qjU&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Complete Meshroom Tutorial | Photogrammetry Course by Gleb Alexandrov")](https://www.youtube.com/watch?v=j3lhPKF8qjU)[![Photoscanning - Camera Settings | Photogrammetry Course by Gleb Alexandrov](https://ytcards.demolab.com/?id=JLdxBtECGuc&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Photoscanning - Camera Settings | Photogrammetry Course by Gleb Alexandrov")](https://www.youtube.com/watch?v=JLdxBtECGuc) 
[![Surveying 02- Photogrammetry & Hydrographic Survey - 30 minute conceptual series I TNPSC JDO 2023](https://ytcards.demolab.com/?id=ZkZbVOdaXHs&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Surveying 02- Photogrammetry & Hydrographic Survey - 30 minute conceptual series I TNPSC JDO 2023")](https://www.youtube.com/watch?v=ZkZbVOdaXHs) 
[![How To Create Accurate Maps With GCP's - Drone Photography](https://ytcards.demolab.com/?id=2yuz4E1_T4o&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "How To Create Accurate Maps With GCP's - Drone Photography")](https://www.youtube.com/watch?v=2yuz4E1_T4o) 
[![DJI Mavic 3 Enterprise - RTK Surveying and Mapping Drone](https://ytcards.demolab.com/?id=bdL6J-q4Owk&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "DJI Mavic 3 Enterprise - RTK Surveying and Mapping Drone")](https://www.youtube.com/watch?v=bdL6J-q4Owk) 
[![Photogrammetry Course: Photoreal 3d With Blender And Reality Capture ](https://ytcards.demolab.com/?id=dWuaIv6UiVQ&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Photogrammetry Course: Photoreal 3d With Blender And Reality Capture")](https://www.youtube.com/watch?v=dWuaIv6UiVQ)[![Which photogrammetry tool is the best ? (3DF Zephyr, Metashape, Reality Capture, Meshroom)](https://ytcards.demolab.com/?id=udXQHys50aA&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Which photogrammetry tool is the best ? (3DF Zephyr, Metashape, Reality Capture, Meshroom)")](https://www.youtube.com/watch?v=udXQHys50aA) 
[![Photogrammetry in Blender and Meshroom - Blender Tutorial](https://ytcards.demolab.com/?id=L_SdlR57NtU&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Photogrammetry in Blender and Meshroom - Blender Tutorial")](https://www.youtube.com/watch?v=L_SdlR57NtU) 
[![Urban photogrammetry | Steps Cottage by 3D Pivot](https://ytcards.demolab.com/?id=E17XQdC3DVU&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Urban photogrammetry | Steps Cottage by 3D Pivot")](https://www.youtube.com/watch?v=E17XQdC3DVU) 
[![RealityCapture to UE5 - Workflow Tutorial](https://ytcards.demolab.com/?id=WrCOhes1Zgg&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "RealityCapture to UE5 - Workflow Tutorial")](https://www.youtube.com/watch?v=WrCOhes1Zgg) 
[![How I 3D scanned a whole freakin' mountain range with a drone | FULL WORKFLOW](https://ytcards.demolab.com/?id=gdd31rgS1q8&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "How I 3D scanned a whole freakin' mountain range with a drone | FULL WORKFLOW")](https://www.youtube.com/watch?v=gdd31rgS1q8)
[![Capturing the World’s OLDEST Stave Church in Unreal Engine 5](https://ytcards.demolab.com/?id=B5hBBFM2I_w&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Capturing the World’s OLDEST Stave Church in Unreal Engine 5")](https://www.youtube.com/watch?v=B5hBBFM2I_w)
[![The Most Photorealistic UNREAL ENGINE 5 Body Cam Demos 4K 2023](https://ytcards.demolab.com/?id=fRmGbM84aOw&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "The Most Photorealistic UNREAL ENGINE 5 Body Cam Demos 4K 2023")](https://www.youtube.com/watch?v=fRmGbM84aOw) 
[![Photogrammetry Survival Guide | Free & Easy | For 3D Printing | Art & Game Assets | Phone or Camera](https://ytcards.demolab.com/?id=TiSGfKm5cFQ&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Photogrammetry Survival Guide | Free & Easy | For 3D Printing | Art & Game Assets | Phone or Camera")](https://www.youtube.com/watch?v=TiSGfKm5cFQ) 
[![Agisoft Metashape - Complete Tutorial (Cloud, Mesh, DSM, DTM, Classify, Orthoimage - No GCPs)](https://ytcards.demolab.com/?id=je79gV8HsZI&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "Agisoft Metashape - Complete Tutorial (Cloud, Mesh, DSM, DTM, Classify, Orthoimage - No GCPs)")](https://www.youtube.com/watch?v=je79gV8HsZI)
[![How AI Photogrammetry Is Changing 3D Forever](https://ytcards.demolab.com/?id=lfWHyi-3VKs&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "How AI Photogrammetry Is Changing 3D Forever")](https://www.youtube.com/watch?v=lfWHyi-3VKs)
[![s Nerf The End of Photogrammetry](https://ytcards.demolab.com/?id=1eJhsTUEPEg&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "s Nerf The End of Photogrammetry")](https://www.youtube.com/watch?v=1eJhsTUEPEg)
[![ONE Thing To Dramatically Improve Your Photogrammetry](https://ytcards.demolab.com/?id=kI-jJUr9rH8&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "ONE Thing To Dramatically Improve Your Photogrammetry")](https://www.youtube.com/watch?v=kI-jJUr9rH8)
[![The Best 3D Scanning Apps for iPhone](https://ytcards.demolab.com/?id=dPOldb5yTdg&lang=en&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&width=240 "The Best 3D Scanning Apps for iPhone")](https://www.youtube.com/watch?v=dPOldb5yTdg)


# Photogrammetry Tools, Libraries, and Frameworks
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

[Autodesk® ReCap™](https://www.autodesk.com/products/recap/free-trial) is a software tool that converts reality captured from laser scans or photos into a 3D model or 2D drawing that's ready to be used in your design built for UAV and drone processes.

[Autodesk® ReCap™ Photo](http://blogs.autodesk.com/recap/introducing-recap-photo/) is a cloud-connected solution tailored for drone/UAV photo capturing workflows. Using ReCap Photo, you can create textured meshes, point clouds with geolocation, and high-resolution orthographic views with elevation maps.

[Pix4D](https://www.pix4d.com/) is a unique suite of photogrammetry software for drone mapping. Capture images with our app, process on desktop or cloud and create maps and 3D models.

[PIX4Dmapper](https://www.pix4d.com/product/pix4dmapper-photogrammetry-software) is the leading photogrammetry software for professional drone mapping.

[RealityCapture](https://www.capturingreality.com/) is a state-of-the-art photogrammetry software solution that creates virtual reality scenes, textured 3D meshes, orthographic projections, geo-referenced maps and much more from images and/or laser scans completely automatically.

[ArcGIS Reality](https://www.esri.com/arcgis/products/arcgis-reality/overview) is a suite of photogrammetry software products designed to enable reality capture workflows for sites, cities, and countries.

[ArcGIS Drone2Map](https://www.esri.com/en-us/arcgis/products/arcgis-drone2map/overview) is the desktop app for your GIS drone mapping needs. As a 2D & 3D photogrammetry app, create the outputs you need.

[Adobe Scantastic](https://labs.adobe.com/projects/scantastic/) is a tool that makes the creation of 3D assets accessible to everyone. It can be used with just a mobile device (combined with Adobe's server-based photogrammetry pipeline), users can easily scan objects in their physical environment and turn them into 3D models which can then be imported into tools like [Adobe Dimension](https://www.adobe.com/products/dimension.html)  and [Adobe Aero](https://www.adobe.com/products/aero.html).

[Adobe Aero](https://www.adobe.com/products/aero.html) is a tool that helps you build, view, and share immersive AR experiences. Simply build a scene by bringing in 2D images from Adobe Photoshop and Illustrator, or 3D models from Adobe Dimension, Substance, third-party apps like Cinema 4D, or asset libraries like Adobe Stock and TurboSquid. Aero optimizes a wide array of assets, including OBJ, GLB, and glTF files, for AR, so you can visualize them in real time.

[Agisoft Metashape](https://www.agisoft.com/) is a stand-alone software product that performs photogrammetric processing of digital images and generates 3D spatial data to be used in GIS applications, cultural heritage documentation, and visual effects production as well as for indirect measurements of objects of various scales.

[MicroStation](https://www.bentley.com/en/products/brands/microstation) is a CAD software platform for 2D and 3D dimensional design and drafting, developed and sold by Bentley Systems. It generates 2D/3D vector graphics objects and elements and includes building information modeling (BIM) features.

[Leica Photogrammetry Suite (LPS)](https://support.hexagonsafetyinfrastructure.com/infocenter/index?page=product&facRef=LPS&facDisp=Leica%20Photogrammetry%20Suite%20(LPS)&landing=1) is a powerful photogrammetry system that delivers full analytical triangulation, the generation of digital terrain models, orthophoto production, mosaicking, and 3D feature extraction in a user-friendly environment that guarantees results even for photogrammetry novices.

[DroneDeploy](https://www.dronedeploy.com/product/photogrammetry/) is a powerful Cloud Photogrammetry platform that provides fast, high-quality results at any scale Upload up to 10,000 images at once without specialized hardware or software Process hundreds of maps simultaneously across your organization Generate precise 2D maps, 3D models, and 360 panoramas.

[Polycam](https://poly.cam/) is the world's most popular LiDAR 3D scanning app for iOS(iPhone/iPad), Web, and Android. It let's you scan the world around you with your mobile device, DSLR camera, or drone to get beautiful, accurate 3D models. 

[Sanborn Prism4D™](https://www.sanborn.com/prism4d/) is a Real-Time Decision Support and Visualization Software that provides integrated command center operation functions within a single turnkey system and performs as a decision support and visualization system for analysis of geospatial information. It includes tools for 2D and 3D visualization that can be integrated with other applications providing a seamless ability to analyze, plan and react in real time to events.

[FlightGoggles](https://flightgoggles.mit.edu/) is a photorealistic sensor simulator for perception-driven robotic vehicles. FlightGoggles provides photorealistic exteroceptive sensor simulation using graphics assets generated with photogrammetry.

[ArcMap Raster Edit Suite](https://github.com/haoliangyu/ares) - is an ArcMap Add-in that enables manual editing of single pixels on raster layer.

[Bertin.js](https://github.com/neocarto/bertin) is a JavaScript library for visualizing geospatial data and make thematic maps for the web.

[CMV - The Configurable Map Viewer](https://github.com/cmv/cmv-app)  is a community-supported open source mapping framework. CMV works with the Esri JavaScript API, ArcGIS Server, ArcGIS Online and more.

[ContextCapture](https://www.bentley.com/software/contextcapture/) is a tool that enables you to automatically generate multi-resolution 3D models at any scale and precision.

[Correlator3D](https://www.simactive.com/correlator3d-mapping-software-features) is a High-end photogrammetry suite.

[FlowEngine](https://aws.amazon.com/marketplace/seller-profile?id=bc1120fb-7263-4683-9301-4b7470f9a2d9) is the perfect photogrammetry Software Development Kit with a powerful, fully customizable photogrammetry reconstruction engine written in C++. 

[FME Desktop](https://www.safe.com/fme/fme-desktop/) is an integrated collection of Spatial ETL tools for data transformation and data translation.

[Geomedia](https://hexagon.com/products/geomedia) is a Commercial GIS software.

[GRASS (Geographic Resources Analysis Support System) GIS](https://grass.osgeo.org/) is a free and open source GIS software.

[SNAP](https://step.esa.int/main/download/snap-download/) is an open source common architecture for ESA Toolboxes ideal for the exploitation of Earth Observation data.

[TerrSet (formerly IDRISI)](https://clarklabs.org/terrset/) is an integrated geographic information system (GIS) and remote sensing software

[The Sentinel Toolbox](https://sentinel.esa.int/web/sentinel/toolboxes) is a collection of processing tools, data product readers and writers and a display and analysis application to process Sentinel data.

[BoofCV](https://github.com/lessthanoptimal/BoofCV) is an open source library written from scratch for real-time computer vision. Its functionality covers a range of subjects, low-level image processing, camera calibration, feature detection/tracking, structure-from-motion, fiducial detection, and recognition. 

[OpenMVG (open Multiple View Geometry)](https://github.com/openMVG/openMVG) is a library for 3D Computer Vision and Structure from Motion. It's targeted for the Multiple View Geometry community.

[Mapnik](http://mapnik.org/) is an open source toolkit for developing mapping applications. It uses a C++ shared library providing algorithms and patterns for spatial data access and visualization.

[Cesium](https://www.cesium.com/) is the foundational open platform for creating powerful 3D geospatial applications.

[CesiumJS](https://cesium.com/cesiumjs/) is a JavaScript library for creating 3D globes and 2D maps in a web browser without a plugin. It uses WebGL for hardware-accelerated graphics, and is cross-platform, cross-browser, and tuned for dynamic-data visualization.

[Cesium ion](https://cesium.com/platform/cesium-ion/) is a robust, scalable, and secure platform for 3D geospatial data. Upload your content and Cesium ion will optimize it as 3D Tiles, host it in the cloud, and stream it to any device. It includes access to curated global 3D content including Cesium World Terrain, Bing Maps imagery, and Cesium OSM Buildings.

[Cesium for Unreal](https://cesium.com/cesium-for-unreal/) is a tool that brings the 3D geospatial ecosystem to Unreal Engine. By combining a high-accuracy full-scale WGS84 globe, open APIs and open standards for spatial indexing such as 3D Tiles, and cloud-based real-world content from Cesium ion with Unreal Engine, this project enables a new era of 3D geospatial software.

[Cesium for O3DE](https://cesium.com/platform/cesium-for-o3de/) is a tool that provides a full-scale, high-accuracy ([WGS84](https://csrc.nist.gov/glossary/term/world_geodetic_system_1984)) globe and runtime 3D Tiles engine for the open source Open 3D Engine (O3DE).

[3D Tiles](https://github.com/CesiumGS/3d-tiles) is an open specification for sharing, visualizing, fusing, and interacting with massive heterogenous 3D geospatial content across desktop, web, and mobile applications.

[TeleSculptor](https://telesculptor.org/) is an open source, cross-platform desktop application for photogrammetry. It was designed specifically with a focus on aerial video processing leveraging video metadata standards ([MISB 0601](https://developer.ridgerun.com/wiki/index.php/LibMISB)) for geolocation, but it can handle both images and video either with or without metadata. TeleSculptor uses structure-from-motion techniques to estimate camera parameters and a sparse set of 3D landmarks.

[Terramodel](https://heavyindustry.trimble.com/products/terramodel) is a powerful software package for the surveyor, civil engineer or contractor who requires a CAD and design package with integrated support for raw survey data.

[MicMac](https://github.com/micmacIGN/micmac) is a free and  open-source photogrammetry software tools for 3D reconstruction.

[3DF Zephyr](https://www.3dflow.net/3df-zephyr-photogrammetry-software/) is a photogrammetry software solution by 3Dflow. It allows you automatically reconstruct 3D models from photos and deal with any 3D reconstruction and scanning challenge. No matter what camera sensor, drone or laser scanner device you are going to use.

[COLMAP](https://colmap.github.io/) is a general-purpose Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipeline with a graphical and command-line interface. It offers a wide range of features for reconstruction of ordered and unordered image collections.

[Multi-View Environment (MVE)](https://www.gcc.tu-darmstadt.de/home/proj/mve/) is an effort to ease the work with multi-view datasets and to support the development of algorithms based on multiple views. It features Structure from Motion, Multi-View Stereo and Surface Reconstruction. MVE is developed at the TU Darmstadt.

[OpenMVG (open Multiple View Geometry)](https://github.com/openMVG/openMVG) is a photogrammtery that provides an end-to-end 3D reconstruction from images framework compounded of libraries, binaries, and pipelines. The libraries provide easy access to features like: images manipulation, features description and matching, feature tracking, camera models, multiple-view-geometry, robust-estimation, and structure-from-motion algorithms.

[DroneDeploy](https://www.dronedeploy.com/) is a drone mapping software for flying your drone to using your data to create interactive maps, 3D models, videos, and more.

[AliceVision](https://github.com/alicevision/AliceVision) is a Photogrammetric Computer Vision Framework which provides 3D Reconstruction and Camera Tracking algorithms. AliceVision comes up with strong software basis and state-of-the-art computer vision algorithms that can be tested, analyzed and reused.

[Meshroom](https://github.com/alicevision/meshroom) is a free, open-source 3D Reconstruction Software based on the AliceVision framework.

[PhotoModeler](https://www.photomodeler.com/) is a software extracts Measurements and Models from photographs taken with an ordinary camera. A cost-effective way for accurate 2D or 3D measurement, photo-digitizing, surveying, 3D scanning, and reality capture.

[OpenDroneMap(ODM)](https://www.opendronemap.org/odm/) is an open source command line toolkit to generate maps, point clouds, 3D models and DEMs from drone, balloon or kite images.

[WebODM](https://www.opendronemap.org/webodm/) is a user-friendly, commercial grade software for drone image processing. Generate georeferenced maps, point clouds, elevation models and textured 3D models from aerial images. It supports multiple engines for processing, currently [ODM](https://github.com/OpenDroneMap/ODM) and [MicMac](https://github.com/dronemapper-io/NodeMICMAC/).

[NodeODM](https://www.opendronemap.org/nodeodm/) is a [standard API specification](https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc) for processing aerial images with engines such as [ODM](https://github.com/OpenDroneMap/ODM). The API is used by clients such as [WebODM](https://github.com/OpenDroneMap/WebODM), [CloudODM](https://github.com/OpenDroneMap/CloudODM) and [PyODM](https://github.com/OpenDroneMap/PyODM).

[ClusterODM](https://www.opendronemap.org/clusterodm/) is a reverse proxy, load balancer and task tracker with optional cloud autoscaling capabilities for NodeODM API compatible nodes. In a nutshell, it's a program to link together multiple NodeODM API compatible nodes under a single network address.

[Mosaic](https://databrickslabs.github.io/mosaic/) is an extension to the Apache Spark framework that allows easy and fast processing of very large geospatial datasets.) is an extension to the Apache Spark framework that allows easy and fast processing of very large geospatial datasets. 

[FIELDimageR](https://www.opendronemap.org/fieldimager/) is an R package to analyze orthomosaic images from agricultural field trials.

[Regard3D](https://www.regard3d.org/) is a free and open source structure-from-motion program. It converts photos of an object, taken from different angles, into a 3D model of this object.

[PhotoCatch](https://apps.apple.com/us/app/photocatch/id1576081762) is the first app for [Apple's Object Capture API](https://developer.apple.com/news/?id=48xhsgu2), enabling anyone to create stunning 3D models in minutes, not days, with no code or 3D experience required.

[PhotoCatch Desktop](https://www.photocatch.app/desktop) is a Professional photogrammetry workstation for exporting beautiful 3D assets ready for Augmented Reality and Visual Effects. It provides performance optimizations for M1 Max and M1 Ultra on MacBook Pro and Mac Studio, so you can process up to 4 3D models at the same time.  

[PhotoCatch Cloud](https://www.photocatch.app/cloud) is a professional service that brings desktop class photogrammetry and 3D editing tools to mobile devices, so you can capture, edit, and share 3D content on-site. It Syncs photo capture with your equipment and use Depth Capture so your 3D models stay the same size as the real world objects.

[Martin](https://martin.maplibre.org/) is a tile server able to generate [vector tiles](https://github.com/mapbox/vector-tile-spec) from large [PostGIS](https://github.com/postgis/postgis) databases on the fly, or serve tiles from [PMTile](https://protomaps.com/blog/pmtiles-v3-whats-new) and [MBTile](https://github.com/mapbox/mbtiles-spec) files. Martin optimizes for speed and heavy traffic, and is written in Rust.

[Headway](https://about.maps.earth/) is a maps stack in a box that makes it easy to take your location data into your own hands. With just a few commands you can bring up your own fully functional maps server. This includes a frontend, basemap, geocoder and routing engine. Choose one of the 200+ predefined cities or provide your own OpenStreetMap extract covering any area: from a neighborhood to the whole planet.

[OpenLayers](https://openlayers.org/) is a high-performance, feature-packed library for creating interactive maps on the web. It can display map tiles, vector data and markers loaded from any source on any web page.

[Supercluster](https://github.com/mapbox/supercluster) is a very fast JavaScript library for geospatial point clustering for browsers and Node.

[MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) is an open-source library for publishing maps on your websites or webview based apps. Fast displaying of maps is possible thanks to GPU-accelerated vector tile rendering. 

[MapLibre Native](https://maplibre.org/) is an Interactive vector tile maps for iOS, Android and other platforms. 

[Maplibre-rs ](https://github.com/maplibre/maplibre-rs) is an Experimental Maps for Web, Mobile and Desktop.

[Prettymaps](https://github.com/marceloprates/prettymaps) is a small set of Python functions to draw pretty maps from OpenStreetMap data. Based on osmnx, matplotlib and shapely libraries. 

[OrientDB](https://github.com/orientechnologies/orientdb) is an Open Source Multi-Model NoSQL DBMS with the support of Native Graphs, Documents Full-Text, Reactivity, Geo-Spatial and Object Oriented concepts.

[PgRouting](https://pgrouting.org/) is a tool that extends the PostGIS / PostgreSQL geospatial database to provide geospatial routing functionality.

[PostGIS Vector Tile Utils](https://github.com/mapbox/postgis-vt-util) is a set of PostgreSQL functions that are useful when creating vector tile sources.

[CMV - The Configurable Map Viewer](https://github.com/cmv/cmv-app)  is a community-supported open source mapping framework. CMV works with the Esri JavaScript API, ArcGIS Server, ArcGIS Online and more.

[ContextCapture](https://www.bentley.com/software/contextcapture/) is a tool that enables you to automatically generate multi-resolution 3D models at any scale and precision.

[Correlator3D](https://www.simactive.com/correlator3d-mapping-software-features) is a High-end photogrammetry suite.

[FME Desktop](https://www.safe.com/fme/fme-desktop/) is an integrated collection of Spatial ETL tools for data transformation and data translation.

[Geomedia](https://hexagon.com/products/geomedia) is a Commercial GIS software.

[GRASS (Geographic Resources Analysis Support System) GIS](https://grass.osgeo.org/) is a free and open source GIS software.

[pyGEDI](https://github.com/EduinHSERNA/pyGEDI) is a high performance, lower cognitive load, and cleaner and more transparent code for data extraction, analysis, processing, and visualization of Global Ecosystem Dynamics Investigation (GEDI) products.

[rGEDI](https://github.com/carlos-alberto-silva/rGEDI) is an R Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing.

[Quick Terrain Modeler](https://appliedimagery.com/) is a proprietary LiDAR exploitation software by Applied Imagery.

[SNAP](https://step.esa.int/main/download/snap-download/) is an open source common architecture for ESA Toolboxes ideal for the exploitation of Earth Observation data.

[The Point Cloud Library (PCL)](https://pointclouds.org/) is a standalone, large scale, open project for 2D/3D image and point cloud processing.

[TopoDOT](https://new.certainty3d.com/) is a proprietary software for extracting topography, 3D models, GIS Assets, and more from point cloud data.

[Treetop](https://github.com/carlos-alberto-silva/weblidar-treetop) is a Shiny-based Application for Extracting Forest Information from LiDAR data.

[TerrSet (formerly IDRISI)](https://clarklabs.org/terrset/) is an integrated geographic information system (GIS) and remote sensing software

[The Sentinel Toolbox](https://sentinel.esa.int/web/sentinel/toolboxes) is a collection of processing tools, data product readers and writers and a display and analysis application to process Sentinel data.

[3D Scanner App for Mac](https://apps.apple.com/us/app/3d-scanner-app/id1419913995) is a desktop tool for processing photos and videos into 3D models using the power of Photogrammetry; which makes it perfect for 3D Design, CAD, Architecture, Games Assets, AR, VR, XR. It shares USDZ models via iMessage to let friends and family see your models in Augmented Reality.

[Cartographer](https://github.com/cartographer-project/cartographer) is a system that provides real-time simultaneous localization and mapping (SLAM) in 2D and 3D across multiple platforms and sensor configurations.

[Tile38](https://tile38.com/) is an open source (MIT licensed), in-memory geolocation data store, spatial index, and realtime geofencing server. It supports a variety of object types including lat/lon points, bounding boxes, XYZ tiles, Geohashes, and GeoJSON.

[OSMnx](https://github.com/gboeing/osmnx) is a Python package that lets you download geospatial data from OpenStreetMap and model, project, visualize, and analyze real-world street networks and any other geospatial geometries. 

[GraphHopper](https://github.com/graphhopper/graphhopper) is a fast and memory-efficient routing engine released under Apache License 2.0. It can be used as a Java library or standalone web server to calculate the distance, time, turn-by-turn instructions and many road attributes for a route between two or more points.

[Rasterio](https://rasterio.readthedocs.io/) is a tool that reads and writes geospatial raster datasets.

[GRASS GIS](https://grass.osgeo.org/) is a Geographic Information System used for geospatial data management and analysis, image processing, graphics/map production, spatial modeling, and visualization.

[Headway](https://about.maps.earth/) is a self-hostable maps stack, powered by OpenStreetMap. This makes it easy to take control of your location data into your own hands. With just a few commands you can bring up your own fully functional maps server. This includes a frontend, basemap, geocoder and routing engine. 

[QGroundControl (QGC)](https://github.com/mavlink/qgroundcontrol) is an intuitive and powerful ground control station (GCS) for UAVs. It provides full flight control and mission planning for any MAVLink enabled drone(Android, iOS, Mac OS, Linux, Windows), and vehicle setup for both PX4 and ArduPilot powered UAVs. 

[GAAS](https://www.gaas.dev/) is an open-source program designed for fully autonomous VTOL(a.k.a flying cars) and drones. GAAS stands for Generalized Autonomy Aviation System. It provides a fully autonomous flight platform based on lidar, HD-map relocalization, path planning, and other modules for aircraft. 

[Fast-Planner](https://github.com/HKUST-Aerial-Robotics/Fast-Planner) is developed aiming to enable quadrotor fast flight in complex unknown environments. It contains a rich set of carefully designed planning algorithms.

[Paparazzi](https://github.com/paparazzi/paparazzi) is a free open source software package for Unmanned (Air) Vehicle Systems. For many years, the system has been used successfuly by hobbyists, universities and companies all over the world, on vehicles of various sizes (11.9g to 25kg). 

[CARMA Platform](https://github.com/usdot-fhwa-stol/carma-platform) is built on robot operating system (ROS) and utilizes open source software (OSS) that enables Cooperative Driving Automation (CDA) features to allow Automated Driving Systems to interact and cooperate with infrastructure and other vehicles through communication. 

[Nerfstudio](https://docs.nerf.studio/) is a tool that provides a simple API that allows for a simplified end-to-end process of creating, training, and testing NeRFs. The library supports a more interpretable implementation of NeRFs by modularizing each component. With more modular NeRFs, we hope to create a more user-friendly experience in exploring the technology. 

[PyTrx](https://github.com/PennyHow/PyTrx) is a Python object-oriented toolbox created for the purpose of calculating real-world measurements from oblique images and time-lapse image series. Its primary purpose is to obtain velocities, surface areas, and distances from imagery of glacial environments.

[Qlone](https://www.qlone.pro/) is a photogrammetry app for creation of 3D models on mobile devices. Qlone is unique in being able to create 3D models on the mobile device without recourse to external cloud servers.

[QGIS](https://github.com/qgis/) is a Free and Open Source Geographic Information System.

[Aerotas](https://www.aerotas.com/) is a tool that processes the data Photogrammetry + Topography + Planimetrics CAD files created from your drone data.

[Topo Setter](https://www.dronemappingtools.com/products/toposetter) is a simple, yet powerful tool for automated postprocessing GNSS data in any coordinate system and replacing coordinates in image EXIF tags with precise coordinates from postprocessed GNSS data. It provides a high level of the input data accuracy.

[TOPODRONE](https://topodrone.com/product/) is a Swiss-based designer and manufacturer of high-precision surveying equipment. They offer a lightweight 360° LiDAR model range with advanced features and capabilities: LiDAR 100 & 100+ with a 100 m working flight altitude and LiDAR 200+ with a 200m working flight altitude. All of them can be used as a single payload for different carriers and installed on a drone, car and backpack. 

[KIRI Engine](https://www.kiriengine.com/) is the World's Most Powerful 3D Scanner App for iOS, Android, and Web Browsers.

[WIDAR](https://www.widar.io/) is a 3D contents creation app that allows you to scan and edit 3D models on your smartphone. Enjoy creating high-quality 3D contents, view directly on device, play in AR and post the contents on in-app community. It can also export 3D contents to use in game, VFX effect in movies, architecture, construction, AR, VR, and 3D printing.

[Trnio](https://www.trnio.com/) is a tool that turns your iPhone to into a high-quality 3D scanner, using our cloud service (scans are NOT processed on your device) to convert your images into high-quality scans.

[Scandy Pro](https://www.scandy.co/apps/scandy-pro) is a 3D scanner tool for iOS/iPadOS that allows users to capture full-color 3D scans. Users can save scans and export scans with different file formats (.stl, .ply, .obj, .glb, .usdz), scales (m, cm, mm, in.), and 3D editor orientations (Zbrush, Blender, Unreal, OpenGL, Maya, CRY, 3DS, Cinema4D, AutoCAD). All rendering is done on-device and there is no need to register or store files in the cloud.

[AR Floorplan 3D](https://arplan3d.com/) is a measurement app, augmented reality (AR, lidar scanner) for quick room measurement. AR camera sensor technology allows to lay virtual tape measure ruler on a real-world surfaces, making measurement process and 3D floor planner creation easier and quicker. Using the device's camera sensor to sketch home, draw blueprints, build design.

# Autodesk Development
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687186-060c4b00-d1ca-11eb-9e90-f51a3ebf4e43.png">
  <br />
</p>

## Autodesk Learning Resources

[Autodesk](https://www.autodesk.com/) is a global leader in design and make technology, with expertise across architecture, engineering, construction, design, manufacturing, and entertainment.

[CNC programming (Computer Numerical Control Programming)](https://www.autodesk.com/solutions/cnc-programming) is utilized by manufacturers to create program instructions for computers to control a machine tool. CNC is highly involved in the manufacturing process and improves automation as well as flexibility.

[AutoDesk Learning & Training](https://www.autodesk.com/training)

[Autodesk Certification](https://www.autodesk.com/certification/overview)

[Autodesk University](https://www.autodesk.com/autodesk-university/)

[Autodesk Design Academy](https://academy.autodesk.com/)

[Autodesk Customer Success Hub](https://customersuccess.autodesk.com)

[Software and Services for Education | Autodesk Education](https://www.autodesk.com/education/home)

[AutoDesk Forums](https://forums.autodesk.com)

[AutoDesk Developer Network](https://www.autodesk.com/developer-network/overview)

[Learning Civil 3D on Autodesk Knowledge Network](https://knowledge.autodesk.com/support/civil-3d/learn)

[Top Autodesk Courses on Udemy](https://www.udemy.com/topic/autodesk/)

[Top Autodesk Courses on Coursera](https://www.coursera.org/autodesk)

[Top Autodesk Fusion 360 Courses on Coursera](https://www.coursera.org/courses?query=autodesk%20fusion%20360&page=1)


## Autodesk Tools and Frameworks

[AutoCAD®](https://www.autodesk.com/products/autocad/overview) is computer-aided design (CAD) software that architects, engineers, and construction professionals rely on to create precise 2D and 3D drawings. It also automates tasks such as comparing drawings, counting, adding blocks, creating schedules.

[AutoCAD LT®](https://www.autodesk.com/products/autocad-lt/overview) is a powerful 2D computer-aided design (CAD) software that architects, engineers, construction professionals, and designers rely on to design, draft, and document with precise 2D geometry.

[AutoCAD® Mobile App](https://www.autodesk.com/products/autocad-mobile/overview) is a mobile(smartphone or tablet) version of AutoCAD that has the core design and drafting tools. Work on your CAD drawings anytime, anywhere—even offline.

[AutoCAD® Web App](https://www.autodesk.com/products/autocad-web-app/overview) is a web version of AutoCAD that can edit, create, share, and view CAD drawings in a web browser on any computer.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687196-0ad0ff00-d1ca-11eb-87d8-6a1e806dcd4c.png">
  <br />
</p>

**AutoCAD® with Architecture toolset. Source: [Autodesk](https://www.autodesk.com/products/autocad/overview)**

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687204-13293a00-d1ca-11eb-806b-57a3526b0b75.png">
  <br />
</p>

**AutoCAD® with  Mechanical toolset. Source: [Autodesk](https://www.autodesk.com/products/autocad/overview)**

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687201-10c6e000-d1ca-11eb-99b4-90dec581f163.png">
  <br />
</p>

**AutoCAD® with Electrical toolset. Source: [Autodesk](https://www.autodesk.com/products/autocad/overview)**

[Tinkercad®](https://www.tinkercad.com) is a free, easy-to-use app for 3D design, electronics, and coding. It's used by teachers, kids, hobbyists, and designers to imagine, design, and make anything.

[Revit®](https://www.autodesk.com/products/revit/overview) is a  BIM (Building Information Modeling) software to drive efficiency and accuracy across the project lifecycle, from conceptual design, visualization, and analysis to fabrication and construction.

[AEC(Architecture, Engineering & Construction) Collection®](https://www.autodesk.com/collections/architecture-engineering-construction/overview) is a set of BIM and CAD tools for designers, engineers, and contractors that is supported by a cloud-based common data environment that facilitates project delivery from early-stage design through to construction.

[Fusion 360®](https://www.autodesk.com/products/fusion-360/overview) is an integrated CAD, CAM, CAE, and PCB software application. It unifies design, engineering, electronics, and manufacturing into a single software platform.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687501-98f9b500-d1cb-11eb-807b-20d24da14fc1.png">
  <br />
</p>

**Autodesk® Fusion 360. Source: [Autodesk](https://www.autodesk.com/products/fusion-360/features#)**

[Fusion 360 with FeatureCAM®](https://www.autodesk.com/products/featurecam/overview) is a tool that gives you access to FeatureCAM Ultimate, PartMaker, Fusion 360, Fusion Team, and HSMWorks. With FeatureCAM CNC programming software uses manufacturing knowledge to intelligently make decisions, produce results, and remove repetitive processes.

[Fusion 360 with Netfabb®](https://www.autodesk.com/products/netfabb/overview) is a software that offers a complete toolset for design and implementation for additive manufacturing. It streamlines workflows and automates processes around 3D print preparation. The software also includes access to Fusion 360, Fusion 360 Team, and additional capabilities through Fusion 360 Additive Extensions.

[Fusion 360 Manage](https://www.autodesk.com/products/fusion-360-manage/overview) is a product lifecycle management platform that connects your people, processes, and data across departments and geographies. It gives you the flexibility to start today and expand tomorrow with PLM that adapts to your business.

[Fusion Team](https://fusionteam.autodesk.com/) is a cloud-based coll tool that helps eliminate the inefficiencies that disparate tools create when working with your internal and external teams.

[Fusion 360 with PowerInspect®](https://www.autodesk.com/products/powerinspect/overview) is a 3D measurement software offers a powerful way to inspect, validate, and manage quality for all measurement equipment. Now includes access to Fusion 360, Fusion 360 Team, and Fusion 360 – Machining Extension. PowerInspect includes comprehensive inspection tools that measure parts while they’re still in On Machine Verification (OMV). Machine tool probing helps you make informed scrap or rework decisions quickly.

[Fusion 360 with PowerMill® CAM](https://www.autodesk.com/products/powermill/overview) is a software provides expert CNC programming strategies for complex 3 and 5-axis manufacturing. This includes access to Fusion 360 and advanced manufacturing capabilities through Fusion 360 extensions.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687213-1f14fc00-d1ca-11eb-931e-79c7c5c58ce9.png">
  <br />
</p>

**CNC machining with Fusion 360 with PowerMill® CAM. Source: [Autodesk](https://www.autodesk.com/products/powermill/overview)**

[Fusion 360 with PowerShape®](https://www.autodesk.com/products/powershape/overview) is a  manufacturing CAD software combines surface, solid, and mesh modeling to help prepare molds, dies, and other complex parts for manufacture. This includes access to Fusion 360 and Fusion 360 Team.

[Autodesk PartMaker®](https://www.autodesk.com/solutions/manufacturing-software/swiss-machining) is a software that can produce CNC programs that drive main and sub-spindle machining operations. These can be used for turning, indexed and interpolated C-axis milling, Y-axis, and B-axis milling.

[Robot Structural Analysis Professional](https://www.autodesk.com/products/robot-structural-analysis/overview) is a structural load analysis software that verifies code compliance and uses BIM-integrated workflows to exchange data with Revit. It can help you to create more resilient, constructible designs that are accurate, coordinated, and connected to BIM.

[Revit LT™](https://www.autodesk.com/products/revit-lt/overview) is a software that provides the most cost-effective BIM (Building Information Modeling) solution, you can produce high-quality 3D architectural designs and documentation.

[Maya®](https://www.autodesk.com/products/maya/overview) is a 3D computer animation, modeling, simulation, and rendering software that can create realistic effects from explosions to cloth simulation.

[Maya LT™](https://www.autodesk.com/products/maya-lt/overview) is a game design software for indie game makers that can create and animate realistic-looking characters, props, and environments using the sophisticated 3D modeling and animation tools.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687226-2a682780-d1ca-11eb-9408-4b32ddc7d493.png">
  <br />
</p>

**Autodesk® Maya. Source:[Autodesk](https://www.autodesk.com/products/maya/overview)**

[3DS Max®](https://www.autodesk.com/products/3ds-max/overview) is a 3D modeling and rendering software for design visualization, games, and animation.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687233-3358f900-d1ca-11eb-8e9c-0cb68b16db0e.png">
  <br />
</p>

**Autodesk® 3DS Max. Source:[Autodesk](https://www.autodesk.com/products/3ds-max/overview)**

[Arnold](https://www.autodesk.com/products/arnold/overview) is an advanced Monte Carlo ray tracing(Global illumination) renderer that helps you work more efficiently.

[ReCap™](https://www.autodesk.com/products/recap/overview) is a Pro 3D scanning software to transform the physical world into a digital asset. With reality capture data you can better understand and verify existing and as-built conditions to gain insights and make better decisions.

[Flame®](https://www.autodesk.com/products/flame/overview) is a 3D VFX and finishing software provides powerful tools for 3D compositing, visual effects, and editorial finishing. An integrated, creative environment means faster compositing, advanced graphics, color correction, and more.

[Mudbox®](https://www.autodesk.com/products/mudbox/overview) is a 3D digital painting and sculpting software that let's you sculpt and paint highly detailed 3D geometry and textures.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687228-2e944500-d1ca-11eb-894e-b55e15c35620.png">
  <br />
</p>

**Autodesk® Mudbox. Source:[Autodesk](https://www.autodesk.com/products/mudbox/overview)**

[Character Generator®](https://www.autodesk.com/products/character-generator/overview) is a powerful 3D design and animation tools, Character Generator offers artists a web-based laboratory to create fully rigged 3D characters for animation packages and game engines.

[Smoke®](https://www.autodesk.com/products/smoke/overview) is a  video effects software helps production studios increase productivity by combining editing workflows with node-based compositing tools in a timeline-centered editing environment.

[ShotGrid](https://www.autodesk.com/products/shotgrid/overview) formerly Shotgun Software, is software for creative project management software and review tools for film, TV, and games that streamlines workflows for creative studios.

[Advance Steel®](https://www.autodesk.com/products/advance-steel/overview) is a 3D modeling software for steel detailing, design, fabrication, and construction. it connects engineers and detailers through a seamless design and detailing workflow between Advance Steel and Revit, you can reduce the time required to move from design to fabrication while simultaneously reducing errors along the way.

[Media & Entertainment Collection®](https://www.autodesk.com/collections/media-entertainment/overview) is a collection that includes all of the tools you need to build a powerful and scalable 3D animation pipeline for complex simulations, effects, and rendering.

[Civil 3D®](https://www.autodesk.com/products/civil-3d/overview) is a  civil engineering design software supports BIM (Building Information Modeling) with integrated features to improve drafting, design, and construction documentation.

[Inventor®](https://www.autodesk.com/products/inventor/overview) is a  CAD software that provides professional-grade 3D mechanical design, documentation, and product simulation tools. Work efficiently with a powerful blend of parametric, direct, freeform, and rules-based design capabilities.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687217-24724680-d1ca-11eb-9768-0fbcba5a0d41.png">
  <br />
</p>

**Autodesk® Inventor. Source:[Autodesk](https://www.autodesk.com/products/inventor/overview)**

[Inventor® CAM](https://www.autodesk.com/products/inventor-cam/overview) is an integrated CAM software for Inventor that simplifies CNC programming processes. Such as the machining workflow with CAD-embedded 2.5-axis to 5-axis milling, turning, and mill-turn capabilities.

[Inventor Nastran®](https://www.autodesk.com/products/inventor-nastran/overview) is a CAD-embedded finite element analysis software that delivers finite element analysis (FEA) tools for engineers and analysts. Simulation covers multiple analysis types, such as linear and nonlinear stress, dynamics, and heat transfer.

[Inventor® Nesting](https://www.autodesk.com/products/inventor-nesting/overview) is a CAD-embedded, true-shape nesting tools for Inventor that helps you optimize yield from flat raw material. Easily compare nesting studies to optimize efficiency and reduce costs, and export 3D models or DXF™ files of the completed nest for cutting path generation.

[Inventor Tolerance Analysis®](https://www.autodesk.com/products/inventor-tolerance-analysis/overview) is an CAD-embedded tolerance stackup analysis software that is designed to help Inventor users make more informed decisions while specifying manufacturing tolerances.

[Product Design & Manufacturing Collection](https://www.autodesk.com/collections/product-design-manufacturing/overview) is an integrated set of professional-grade applications that connect everyone, from concept to production, with shared tools to streamline your product development process.

[Navisworks®](https://www.autodesk.com/products/navisworks/overview) is a project review software to improve BIM (Building Information Modeling) coordination. That can combine design and construction data into a single model.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/122687230-2f2cdb80-d1ca-11eb-9bcf-5dc2fb858d7d.png">
  <br />
</p>

**Autodesk® Navisworks. Source:[Autodesk](https://www.autodesk.com/products/navisworks/overview)**

[BIM Collaborate](https://www.autodesk.com/products/bim-collaborate/overview) is cloud-based design collaboration and coordination software that connects AEC teams, helping you execute on design intent and deliver high-quality constructible models on a single platform.

[BIM Collaborate Pro](https://www.autodesk.com/products/bim-collaborate/overview) is cloud-based design collaboration and coordination software that connects AEC teams, helping you execute on design intent and deliver high-quality constructible models on a single platform.

[InfraWorks®](https://www.autodesk.com/products/infraworks/overview) is a conceptual design software lets architecture, engineering, and construction professionals model, analyze, and visualize infrastructure design concepts within the context of the built and natural environment—improving decision making and accelerating project approvals.

[SketchBook®](https://www.autodesk.com/products/sketchbook/overview) is a drawing and painting software lets designers, architects, and concept artists sketch ideas quickly and create stunning illustrations.

[Alias®](https://www.autodesk.com/products/alias-products/overview) is a product design software for sketching, concept modeling, surfacing, visualization. It can create and reuse templates across design and surfacing teams sharing surfacing language.

[Assemble BIM Data](https://construction.autodesk.com/products/assemble/) is a tool that helps keep projects on track. Along with condition and connect BIM data to design reviews, estimating, change management, scheduling, work-in-place tracking, and more.

[Autodesk® Forge](https://forge.autodesk.com) is a cloud-based developer platform from Autodesk. That let's you access design and engineering data in the cloud with the Forge platform. Whether you want to automate processes, connect teams and workflows, or visualize your data using Forge APIs.

[Autodesk® Rendering](https://www.autodesk.com/products/rendering/overview) is a fast, high-resolution cloud rendering software that let's you produce stunning, high-quality renderings from designs and models with cloud rendering. This service uses cloud credits, which is a universal measure across Autodesk consumption-based cloud services to perform certain tasks in the cloud.

[Autodesk® CFD](https://www.autodesk.com/products/cfd/overview) is a computational fluid dynamics simulation software that engineers and analysts use to intelligently predict how liquids and gases will perform. It helps to minimize the need for physical prototypes while providing deeper insight into fluid flow design performance.

[Autodesk® Drive](https://www.autodesk.com/subscription/drive) is a way to securely store, preview, and share your 2D and 3D design data.

[Autodesk® Viewer](https://www.autodesk.com/viewers) is a tool that supports most 2D and 3D files, including DWG, STEP, DWF, RVT, and Solidworks, and works with over 80 file types on any device. Get the feedback you need with Autodesk Viewer’s annotation and drawing tools for easy online collaboration.

[Autodesk BIM 360®](https://www.autodesk.com/bim-360/) is a tool is part of the Autodesk Construction Cloud, connecting workflows, teams, and data to help you build better.

[Autodesk® Build](https://construction.autodesk.com/products/autodesk-build/) is a construction management software for field execution and project management that empowers you to seamlessly collaborate and deliver construction projects on time, on budget.

[Autodesk® Takeoff](https://construction.autodesk.com/products/autodesk-takeoff/) is a tool that helps you work with competitive bids that are generated from accurate estimates produced from integrated 2D takeoffs and 3D quantities.

[BuildingConnected](https://www.buildingconnected.com) is the argest real-time construction network that connects owners and builders through an easy-to-use platform to streamline the bid and risk management process.

[Bid Board Pro](https://www.buildingconnected.com/bid-board/) is a tool that helps you see all bid invites across your entire office or division from one place. Know what needs to get done, who’s responsible for it and when it’s due. Track project files, deadlines and more during each stage of the bidding process.

[TradeTapp](https://www.buildingconnected.com/tradetapp/) is a tool that helps you significantly decrease the time it takes to analyze subcontractor risk, annually or for a specific project. Advanced risk profiles enable a streamlined process and offer financial benchmarking, key metric calculations, capacity recommendations and safety performance history.

[Design Review](https://www.autodesk.com/products/design-review/overview) is a CAD viewer software lets you view, mark up, print, and track changes to 2D and 3D files for free—without the original design software. Work with a variety of file formats, including: DWF, DWFx, DWG, and DXF (requires installation of [free DWG TrueView software](https://www.autodesk.com/products/dwg/viewers)); Adobe PDF; as well as image file types such as.bmp, .jpg, .gif, .pcx, .pct, .png, .rlc, .tga, .tif, .mil, .cal, and more.

[EAGLE](https://www.autodesk.com/products/eagle/overview) is electronic design automation (EDA) software that lets printed circuit board (PCB) designers seamlessly connect schematic diagrams, component placement, PCB routing, and comprehensive library content.

[Fabrication ESTmep™, CADmep™, and CAMduct™](https://www.autodesk.com/products/fabrication/overview) is a software that provides an integrated set of tools for MEP specialty contractors to estimate, detail, and drive fabrication of mechanical building systems. Also, create high LOD models of piping, plumbing, or ductwork systems in AutoCAD using CADmep. Content libraries used in ESTmep, CADmep, and CAMduct can also be used in Revit to support BIM workflows. Available stand-alone or in the Architecture, Engineering & Construction Collection..

[Formit](https://www.autodesk.com/products/formit/overview) is an architectural modeling software for BIM-based 3D sketching. The pro version of FormIt includes the tools in the FormIt app, plus Dynamo computation, and collaboration and analysis features.

[Helius Composite](https://www.autodesk.com/products/helius-composite/overview) is a tool that can help you simulate the material behavior of compound components. Built-in solvers minimize the need to have secondary finite element analysis (FEA) software to analyze material characteristics more quickly.

[Helius PFA](https://www.autodesk.com/products/helius-pfa/overview) is a progressive failure analysis software that predicts failure stages of composite materials. Helius PFA enables you to integrate composite and elastomeric material properties into your finite element analysis (FEA) program.

[HSMWorks](https://www.autodesk.com/products/hsmworks/overview) is an ambedded CAM software for [SOLIDWORKS®](https://www.solidworks.com/) to design and generate CAM toolpaths without the hassle of changing software. Reduce cycle time and rework with CAD-embedded 2.5 to 5-axis milling, turning, and mill-turn capabilities. HSMWorks is included with your Fusion 360 subscription.

[Insight](https://www.autodesk.com/products/insight/overview) is a building performance analysis software that empowers architects and engineers to design more energy-efficient buildings with advanced simulation engines and building performance analysis data integrated in Revit.

[Moldflow®](https://www.autodesk.com/products/moldflow/overview) is a software tool that lets you troubleshoot problems with plastic injection and compression molding for design and manufacturing. Advanced tools and a simplified user interface help you address manufacturing challenges, such as part warpage, cooling channel efficiency, and cycle time reduction.

[MotionBuilder®](https://www.autodesk.com/products/motionbuilder/overview) is a 3D character animation software. Work in an interactive environment optimized to help you work faster and more efficiently without compromising creativity.

[PlanGrid Build](https://construction.autodesk.com/products/autodesk-plangrid-build/?pgr=1) is a Construction app built for the field. It allows you to complete tasks from anywhere on the jobsite with seamless access to Autodesk Build data, even when you’re offline.

[Point Layout](https://www.autodesk.com/products/point-layout/overview) is a  construction layout software helps contractors and subcontractors bring model accuracy to the field and back. Connect models to layout and quality workflows. Get direct file format compatibility with robotic total station hardware, including Leica, Topcon, and Trimble.

[Structural Bridge Design®](https://www.autodesk.com/products/structural-bridge-design/overview) is a bridge analysis software for small to medium-span bridges used by engineers to deliver design reports faster.

[Vault®](https://www.autodesk.com/products/vault/overview) is a product data management (PDM) software helps streamline workflows. Everyone works from a central source of organized data—collaborating, reducing errors, and saving time.

[Vehicle Tracking®](https://www.autodesk.com/products/vehicle-tracking/overview) is a swept path analysis and design software to facilitate parking lot layout, roundabout design, and other design challenges impacted by vehicle movement.

[VRED®](https://www.autodesk.com/products/vred/overview) is a 3D visualization software helps automotive designers and engineers create product presentations, design reviews, and virtual prototypes using interactive GPU raytracing and both analytic and cloud-rendering modes.

[Within Medical®](https://www.autodesk.com/products/within-medical/overview) is a 3D printing orthopedic implant design software that enables designers to create medical implants to aid osseointegration.

[Pype](https://construction.autodesk.com/products/pype/) is a tool that helps you reduce project risk and strengthen client relationships by automating processes that are critical for owner satisfaction and contract compliance.

[Pype Closeout](https://pype.io/closeout/) is a tool provides a single portal for closeout documentation management, with digital document collection from subcontractors and powerful reporting dashboards. With subcontractor outreach automated, the Closeout platform ensures contract compliance and helps you get paid faster.

[Pype SmartPlans](https://pype.io/smartplans/) is a tool that locates and extracts all submittals from your uploaded plans automatically. Export product, equipment, and finish schedules into excel with a single click. SmartPlans’ powerful automation uses cutting edge artificial intelligence and machine learning to intelligently read your drawings to extract submittals and schedules.

[CAMplete](https://www.autodesk.com/products/camplete/overview) is a software tool that  provides G-code post-processing, verification, and simulation for different kinds of CNC machinery. Import data from leading CAM software then use proven post-processors and highly accurate 3D machine models, developed in partnership with machine tool builders, to rapidly produce high-quality, collision free NC machining code.

[Vault PLM](https://www.autodesk.com/products/vault-plm/overview) is a tool that combines Vault Professional with Fusion Lifecycle for enterprise-wide collaboration and product lifecycle management.

# LiDAR Development
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950812-f5ae2900-cd0e-11eb-8989-9188bd18a68c.png">
  <br />
</p>

## LiDAR Learning Resources
[Back to the Top](https://github.com/mikeroyal/LiDAR-Guide#table-of-contents)

[Introduction to Lidar Course - NOAA](https://coast.noaa.gov/digitalcoast/training/intro-lidar.html)

[Lidar 101:An Introduction to Lidar Technology, Data, and Applications(PDF) - NOAA](https://coast.noaa.gov/data/digitalcoast/pdf/lidar-101.pdf)

[Understanding LiDAR Technologies - GIS Lounge](https://www.gislounge.com/understanding-lidar-technologies/)

[LiDAR University Free Lidar Training Courses on MODUS AI](https://www.modus-ai.com/lidar-university-2/)

[LiDAR | Learning Plan on ERSI](https://www.esri.com/training/catalog/5bccd52a6e9c0f01fb49e85d/lidar/#!)

[Light Detection and Ranging Sensors Course on Coursera](https://www.coursera.org/lecture/state-estimation-localization-self-driving-cars/lesson-1-light-detection-and-ranging-sensors-3NXgp)

[Quick Introduction to Lidar and Basic Lidar Tools(PDF)](https://training.fws.gov/courses/references/tutorials/geospatial/CSP7304/documents/Lidar.pdf)

[LIDAR - GIS Wiki](http://wiki.gis.com/wiki/index.php/Lidar)

[OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/Main_Page)

[OpenStreetMap Frameworks](https://wiki.openstreetmap.org/wiki/Frameworks)

## LiDAR Tools & Frameworks

[Light Detection and Ranging (lidar)](https://www.usgs.gov/news/earthword-lidar) is a technology used to create high-resolution models of ground elevation with a vertical accuracy of 10 centimeters (4 inches). Lidar equipment, which includes a laser scanner, a Global Positioning System (GPS), and an Inertial Navigation System (INS), is typically mounted on a small aircraft. The laser scanner transmits brief pulses of light to the ground surface. Those pulses are reflected or scattered back and their travel time is used to calculate the distance between the laser scanner and the ground.  Lidar data is initially collected as a “point cloud” of individual points reflected from everything on the surface, including structures and vegetation. To produce a “bare earth” Digital Elevation Model (DEM), structures and vegetation are stripped away.

 <p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950840-fe9efa80-cd0e-11eb-9a12-57c4799d63b5.png">
  <br />
</p>

**3D Data Visualization of Golden Gate Bridge. Source: [USGS](https://www.usgs.gov/core-science-systems/ngp/tnm-delivery)**

[Mola](https://docs.mola-slam.org/latest/) is a Modular Optimization framework for Localization and mApping (MOLA).

 <p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950850-01015480-cd0f-11eb-9fa6-1f93d6d87cd1.gif">
  <br />
</p>

**3D LiDAR SLAM from KITTI dataset. Source: [MOLA](https://docs.mola-slam.org/latest/demo-kitti-lidar-slam.html)**

[Lidar Toolbox™](https://www.mathworks.com/products/lidar.html) is a MATLAB tool that provides algorithms, functions, and apps for designing, analyzing, and testing lidar processing systems. You can perform object detection and tracking, semantic segmentation, shape fitting, lidar registration, and obstacle detection. Lidar Toolbox supports lidar-camera cross calibration for workflows that combine computer vision and lidar processing.

[Automated Driving Toolbox™](https://www.mathworks.com/products/automated-driving.html) is a MATLAB tool that provides algorithms and tools for designing, simulating, and testing ADAS and autonomous driving systems. You can design and test vision and lidar perception systems, as well as sensor fusion, path planning, and vehicle controllers. Visualization tools include a bird’s-eye-view plot and scope for sensor coverage, detections and tracks, and displays for video, lidar, and maps. The toolbox lets you import and work with HERE HD Live Map data and OpenDRIVE® road networks. It also provides reference application examples for common ADAS and automated driving features, including FCW, AEB, ACC, LKA, and parking valet. The toolbox supports C/C++ code generation for rapid prototyping and HIL testing, with support for sensor fusion, tracking, path planning, and vehicle controller algorithms.

[Microsoft AirSim](https://microsoft.github.io/AirSim/lidar.html) is a simulator for drones, cars and more, built on Unreal Engine (with an experimental Unity release). AirSim is open-source, cross platform, and supports [software-in-the-loop simulation](https://www.mathworks.com/help///ecoder/software-in-the-loop-sil-simulation.html) with popular flight controllers such as PX4 & ArduPilot and [hardware-in-loop](https://www.ni.com/en-us/innovations/white-papers/17/what-is-hardware-in-the-loop-.html) with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. AirSim is being developed  as a platform for AI research to experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles.

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/121950853-02328180-cd0f-11eb-9459-1b31d084bd3f.png">
  <br />
</p>

**3D Autonomous Vehicle Simulation in AirSim. Source: [Microsoft](https://microsoft.github.io/AirSim)**

[LASer(LAS)](https://www.asprs.org/divisions-committees/lidar-division/laser-las-file-format-exchange-activities) is a public file format for the interchange of 3-dimensional point cloud data data between data users. Although developed primarily for exchange of lidar point cloud data, this format supports the exchange of any 3-dimensional x,y,z tuplet. This binary file format is an alternative to proprietary systems or a generic ASCII file interchange system used by many companies. The problem with proprietary systems is obvious in that data cannot be easily taken from one system to another. There are two major problems with the ASCII file interchange. The first problem is performance because the reading and interpretation of ASCII elevation data can be very slow and the file size can be extremely large even for small amounts of data. The second problem is that all information specific to the lidar data is lost. The LAS file format is a binary file format that maintains information specific to the lidar nature of the data while not being overly complex.

[3D point cloud](https://www.onyxscan-lidar.com/point-cloud/) is a set of data points defined in a given three-dimensional coordinates system.. Point clouds can be produced directly by 3D scanner which records a large number of points returned from the external surfaces of objects or earth surface. These data are exchanged between LiDAR users mainly through LAS format files (.las).

[ArcGIS Desktop](https://www.esri.com/en-us/arcgis/products/arcgis-desktop/overview) is powerful and cost-effective desktop geographic information system (GIS) software. It is the essential software package for GIS professionals. ArcGIS Desktop users can create, analyze, manage, and share geographic information so decision-makers can make intelligent, informed decisions.

[USGS 3DEP Lidar Point Cloud Now Available as Amazon Public Dataset](https://www.usgs.gov/news/usgs-3dep-lidar-point-cloud-now-available-amazon-public-dataset)

[National Geospatial Program](https://www.usgs.gov/core-science-systems/national-geospatial-program)

[National Map Data Download and Visualization Services](https://www.usgs.gov/core-science-systems/ngp/tnm-delivery)

[USGS Lidar Base Specification(LBS) online edition](https://www.usgs.gov/core-science-systems/ngp/ss/lidar-base-specification-online)

# Game Development
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/97361059-45151700-185c-11eb-9d12-dae51c79eb8a.png">
  <br />
</p>

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/119279021-ea6b5000-bbdd-11eb-9f59-5251fc3ac751.png">
  <br />
</p>

## Game Engines

**[Checkout the Unity Engine](https://unity.com/)**

<img src="https://user-images.githubusercontent.com/45159366/104788113-3432be00-5746-11eb-99b1-49360669f327.png">


**[Checkout the Unreal Engine 4](https://www.unrealengine.com/)**

<img src="https://user-images.githubusercontent.com/45159366/104788122-37c64500-5746-11eb-8f61-48a69b94582d.png">


**[Checkout the CryEngine](https://www.cryengine.com/)**

<img src="https://user-images.githubusercontent.com/45159366/104788177-680de380-5746-11eb-9fc2-6d6f0bdc0a82.png">


**[Checkout the Godot Engine](https://godotengine.org/)**

[If you would like to Donate to the Godot Project](https://www.patreon.com/godotengine)

<img src="https://user-images.githubusercontent.com/45159366/104788134-3f85e980-5746-11eb-94c4-d97165ee888b.jpeg">


**[Checkout Blender](https://www.blender.org/)**

[If you would like to Donate to the Blender Project](https://fund.blender.org/)

<img src="https://user-images.githubusercontent.com/45159366/104788139-401e8000-5746-11eb-9647-058dee01a00e.png">


**[Checkout AWS Lumberyard(based on CryEngine)](https://aws.amazon.com/lumberyard/)**

<img src="https://user-images.githubusercontent.com/45159366/104788145-43b20700-5746-11eb-82f1-1351c3b7e380.png">


**[Checkout Game Maker Studio 2](https://www.yoyogames.com/gamemaker)**

<img src="https://user-images.githubusercontent.com/45159366/104788147-44e33400-5746-11eb-879a-bc6239c98ce4.jpg">


## Game Development Learning Resources

[Unreal Online Learning](https://www.unrealengine.com/en-US/onlinelearning-courses) is a free learning platform that offers hands-on video courses and guided learning paths.

[Unreal Engine Authorized Training Program](https://www.unrealengine.com/en-US/training-partners)

[Unreal Engine for education](https://www.unrealengine.com/en-US/education/)

[Unreal Engine Training & Simulation](https://www.unrealengine.com/en-US/industry/training-simulation)

[Unity Certifications](https://unity.com/products/unity-certifications)

[Autodesk for Games](https://www.autodesk.com/campaigns/autodesk-for-games)

[Getting Started with DirectX 12 Ultimate](https://devblogs.microsoft.com/directx/directx-12-ultimate-getting-started-guide/)

[Getting Started with Vulkan](https://www.khronos.org/vulkan/)

[Getting Started with Apple Metal](https://developer.apple.com/metal/)

[Game Design Online Courses from Udemy](https://www.udemy.com/courses/Design/Game-Design/)

[Game Design Online Courses from Skillshare](https://www.skillshare.com/browse/game-design)

[Learn Game Design with Online Courses and Classes from edX](https://www.edx.org/learn/game-design)

[Game Design Courses from Coursera](https://www.coursera.org/courses?query=game%20design)

[Game Design and Development Specialization Course from Coursera](https://www.coursera.org/specializations/game-development)

## Game Development Tools

[Unreal Engine](https://www.unrealengine.com) is a game engine developed by Epic Games with the world's most open and advanced real-time 3D creation tool. Continuously evolving to serve not only its original purpose as a state-of-the-art game engine, today it gives creators across industries the freedom and control to deliver cutting-edge content, interactive experiences, and immersive virtual worlds.

[Unity](https://unity.com) is a cross-platform game development platform. Use Unity to build high-quality 3D and 2D games, deploy them across mobile, desktop, VR/AR, consoles or the Web, and connect with loyal and enthusiastic players and customers.

[Unigine](https://unigine.com) is a cross-platform game engine designed for development teams (C++/C# programmers, 3D artists) working on interactive 3D apps.

[Panda3D](https://www.panda3d.org/) is a game engine, a framework for 3D rendering and game development for Python and C++ programs, developed by Disney and CMU. Panda3D is open-source and free for any purpose, including commercial ventures.

[Source 2](https://developer.valvesoftware.com/wiki/Source_2) is a 3D video game engine in development by Valve as a successor to Source. It is used in Dota 2, Artifact, Dota Underlords, parts of The Lab, SteamVR Home, and Half-Life: Alyx.

[Havok](https://www.havok.com/) is a middleware software suite that provides a realistic physics engine component and related functions to video games. It is supported  and optimized across all major platforms, including Nintendo Switch, PlayStation®, Stadia, and Xbox. Along with integrations for Unity and Unreal Engine and are used in countless proprietary game engines.

[AutoDesk 3ds Max](https://www.autodesk.com/products/3ds-max/overview) is a professional software program for 3D modeling, animation, rendering, and visualization. 3ds Max allows you to create stunning game environments, design visualizations, and virtual reality experiences.

[Houdini](https://www.sidefx.com/) is a 3D procedural software for modeling, rigging, animation, VFX, look development, lighting and rendering in film, TV, advertising and video game pipelines.

[A-Frame](https://aframe.io) is a web framework for building virtual reality experiences in WebVR with HTML and Entity-Component. A-Frame works on Vive, Rift, desktop, mobile platforms.

[AppGameKit](https://www.appgamekit.com) is a powerful game development engine, ideal for Hobbyist and Indie developers. Where you can start coding in the easy to learn AppGameKit BASIC or use the libraries in C++ & XCode.

[Amazon Lumberyard](https://aws.amazon.com/lumberyard/) is an open source, AAA game engine(based on CryEngine) that gives you the tools you need to create high quality games. Deeply integrated with AWS and Twitch, Amazon Lumberyard includes full source code, allowing you to customize your project at any level.

[Blender](https://www.blender.org) is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, video editing and 2D animation pipeline.

[CryEngine](https://www.cryengine.com) is a powerful real-time game development platform created by Crytek.

[GameMaker Studio 2](https://www.yoyogames.com/gamemaker) is the latest and greatest incarnation of GameMaker. It has everything you need to take your idea from concept to finished game. With no barriers to entry and powerful functionality, GameMaker Studio 2 is the ultimate 2D development environment.

[Godot](https://godotengine.org) is a feature-packed, cross-platform game engine to create 2D and 3D games from a unified interface. It provides a comprehensive set of common tools, so that users can focus on making games without having to reinvent the wheel. Games can be exported in one click to a number of platforms, including the major desktop platforms (Linux, Mac OSX, Windows) as well as mobile (Android, iOS) and web-based (HTML5) platforms.

[Open Graphics Library(OpenGL)](https://www.opengl.org/) is an API used acrossed mulitple  programming languages and platforms for hardware-accelerated rendering of 2D/3D vector graphics currently developed by the [Khronos Group](https://www.khronos.org/).

[Open Computing Language (OpenCL)](https://www.khronos.org/opencl/) is an open standard for [parallel programming](https://www.coursera.org/lecture/parprog1/introduction-to-parallel-computing-zNrIS) of heterogeneous platforms consisting of CPUs, GPUs, and other hardware accelerators found in supercomputers, cloud servers, personal computers, mobile devices and embedded platforms.

[OpenGL Shading Language(GLSL)](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL)) is a High Level Shading Language based on the C-style language, so it covers most of the features a user would expect with such a language.  Such as control structures (for-loops, if-else statements, etc) exist in GLSL, including the switch statement.

[High Level Shading Language(HLSL)](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl) is the High Level Shading Language for DirectX. Using HLSL, the user can create C-like programmable shaders for the Direct3D pipeline. HLSL was first created with DirectX 9 to set up the programmable 3D pipeline.

[DirectX 12 Ultimate](https://github.com/Microsoft/DirectX-Graphics-Samples) is an API(for high performance 2D & 3D graphics) from Microsoft. DirectX 12 Ultimate brings support for ray tracing, mesh shaders, variable rate shading, and sampler feedback. Available in Windows 2004 version(May 2020 Update).

[Vulkan](https://www.khronos.org/vulkan/) is a modern cross-platform graphics and compute API that provides high-efficiency, cross-platform access to modern GPUs used in a wide variety of devices from PCs and consoles to mobile phones and embedded platforms. Vulkan is currently in development by the Khronos consortium.

[Metal](https://developer.apple.com/metal/) is a low-level GPU programming framework used for rendering 2D and 3D graphics on Apple platforms such as iOS, iPadOS, macOS, watchOS and tvOS.

[MoltenVK](https://moltengl.com/moltenvk) is an implementation of Vulkan running on iOS and macOS using Apple's [Metal](https://developer.apple.com/metal/) graphics framework.

[MoltenGL](https://moltengl.com) is an implementation of the OpenGL ES 2.0 API that runs on Apple's [Metal](https://developer.apple.com/metal/) graphics framework.

[Mesa 3D Graphics Library](https://docs.mesa3d.org/index.html) is a project began as an open-source implementation of the OpenGL specification. A system for rendering interactive 3D graphics. Mesa ties into several other open-source projects: the [Direct Rendering Infrastructure](https://dri.freedesktop.org/), [X.org](https://x.org/), and [Wayland](https://wayland.freedesktop.org/) to provide OpenGL support on Linux, FreeBSD, and other operating systems.

[OpenGL ES](https://www.khronos.org/opengles/) is the mobile subset of OpenGL. It's supported on all major mobile platforms, and is also the base for WebGL.

[OpenCL](https://www.khronos.org/opencl/) is a framework for writing programs that execute across heterogeneous platforms consisting of CPUs, GPUs, DSPs, FPGAs and other processors or hardware accelerators.

[EGL](https://www.khronos.org/egl/) is an interface between Khronos rendering APIs such as OpenGL or OpenVG and the underlying native platform window system.

[VDPAU](https://www.freedesktop.org/wiki/Software/VDPAU/) is the Video Decode and Presentation API for UNIX. It provides an interface to video decode acceleration and presentation hardware present in modern GPUs.

[VA API](https://freedesktop.org/wiki/Software/vaapi/) is an open-source library and API specification, which provides access to graphics hardware acceleration capabilities for video processing.

[XvMC](https://en.wikipedia.org/wiki/X-Video_Motion_Compensation) is an extension of the X video extension (Xv) for the X Window System. The XvMC API allows video programs to offload portions of the video decoding process to the GPU hardware.

[AMD Radeon ProRender](https://www.amd.com/en/technologies/radeon-prorender) is a powerful physically-based rendering engine that enables creative professionals to produce stunningly photorealistic images on virtually any GPU, any CPU, and any OS in over a dozen leading digital content creation and CAD applications.

[NVIDIA Omniverse](https://developer.nvidia.com/nvidia-omniverse-platform) is a powerful, multi-GPU, real-time simulation and collaboration platform for 3D production pipelines based on Pixar's Universal Scene Description and NVIDIA RTX.

[LibGDX](https://github.com/libgdx/libgdx) is a cross-platform Java game development framework based on OpenGL (ES) that works on Windows, Linux, Mac OS X, Android, your WebGL enabled browser and iOS.

[cocos2d-x](https://github.com/cocos2d/cocos2d-x) is a multi-platform framework for building 2d games, interactive books, demos and other graphical applications. It is based on cocos2d-iphone, but instead of using Objective-C, it uses C++. It works on iOS, Android, macOS, Windows and Linux.

[MonoGame](https://github.com/MonoGame/MonoGame) is a framework for creating powerful cross-platform games. The spiritual successor to XNA with thousands of titles shipped across desktop, mobile, and console platforms. MonoGame is a fully managed .NET open source game framework without any black boxes.

[Three.js](https://threejs.org) is a cross-browser JavaScript library and application programming interface used to create and display animated 3D computer graphics in a web browser using WebGL.

[Superpowers](http://superpowers-html5.com/) is a downloadable HTML5 app for real-time collaborative projects . You can use it solo like a regular offline game maker, or setup a password and let friends join in on your project through their Web browser.

[URHO3D](https://urho3d.github.io/) is a free lightweight, cross-platform 2D and 3D game engine implemented in C++ and released under the MIT license. Greatly inspired by OGRE and Horde3D.

[Vivox](https://www.vivox.com/) is a voice & text chat platform that's trusted by the world's biggest gaming brands and titles such as Fortnite, PUBG, League of Legends, and Rainbow Six Siege.

[HGIG](https://www.hgig.org/) is a volunteer group of companies from the game and TV display industries that meet to specify and make available for the public guidelines to improve consumer gaming experiences in HDR.

[GameBlocks](https://www.gameblocks.com/) is a Server Side Anti-Cheat & Middleware software.

## Augmented Reality (AR) & Virtual Reality (VR)

[ARKit](https://developer.apple.com/augmented-reality/arkit/) is a set set of software development tools to enable developers to build augmented-reality apps for iOS developed by Apple. The latest version ARKit 3.5 takes advantage of the new LiDAR Scanner and depth sensing system on iPad Pro(2020) to support a new generation of AR apps that use Scene Geometry for enhanced scene understanding and object occlusion.

[RealityKit](https://developer.apple.com/documentation/realitykit) is a framework to implement high-performance 3D simulation and rendering with information provided by the ARKit framework to seamlessly integrate virtual objects into the real world.

[SceneKit](https://developer.apple.com/scenekit/) is a high-level 3D graphics framework that helps you create 3D animated scenes and effects in your iOS apps.

[ARCore](https://developers.google.com/ar/) is a software development kit developed by Google that allows for augmented reality applications in the real world. These tools include environmental understanding, which allows devices to detect horizontal and vertical surfaces and planes. It also includes motion tracking, which lets phones understand and track their positions relative to the world. Also ARCore’s Light Estimation API lets your digital objects appear realistically as if they’re actually part of the physical world.

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/117720758-e843d300-b193-11eb-9796-bde15aebed71.png">
<br />
</p>

Microsoft HoloLens Headset. Source: [Microsoft](https://www.microsoft.com/en-us/hololens/buy)

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/117720763-e9750000-b193-11eb-888a-e4bccd6c30eb.png">
<br />
</p>

PlayStation VR Headset. Source: [PlayStation](https://www.playstation.com/en-us/ps-vr/)

[SteamVR](https://store.steampowered.com/steamvr) is the ultimate tool for experiencing VR content on the hardware of your choice. SteamVR supports the Valve Index, HTC Vive, Oculus Rift, Windows Mixed Reality headsets, and others.

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/110881514-543db400-8295-11eb-9543-fd5d385ddb05.png">
<br />

SteamVR Home
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/45159366/117720776-ed088700-b193-11eb-8538-9831999b5104.png">
<br />
</p>
Valve Index VR Headset. Source: [Steam](https://store.steampowered.com/valveindex)


[OpenVR](https://github.com/ValveSoftware/openvr) is an API and runtime that allows access to VR hardware(Steam Index, HTC Vive, and Oculus Rift) from multiple vendors without requiring that applications have specific knowledge of the hardware they are targeting.

[OpenVR Benchmark on Steam](https://store.steampowered.com/app/955610/OpenVR_Benchmark/) is the first benchmark tool for reproducibly testing your real VR performance, rendering inside of your VR headset.

[OpenHMD](http://www.openhmd.net/) is open source API and drivers that supports a wide range of HMD(head-mounted display) devices such as Oculus Rift, HTC Vive, Sony PSVR, and others.

[openXR](https://www.khronos.org/OpenXR/) is a free, open standard that provides high-performance access to Augmented Reality (AR) and Virtual Reality (VR) collectively known as XR—platforms and devices.

[Monado](https://monado.dev/) is the first OpenXR™ runtime for GNU/Linux. Monado aims to jump-start development of an open source XR ecosystem and provide the fundamental building blocks for device vendors to target the GNU/Linux platform.

[Libsurvive](https://github.com/cntools/libsurvive) is a set of tools and libraries that enable 6 dof tracking on lighthouse and vive based systems that is completely open source and can run on any device. It currently supports both SteamVR 1.0 and SteamVR 2.0 generation of devices and should support any tracked object commercially available.

[Simula](https://github.com/SimulaVR/Simula) is a VR window manager for Linux that runs on top of Godot. It takes less than 1 minute to install. Simula is officially compatible with SteamVR headsets equipped with Linux drivers (e.g. HTC Vive, HTC Vive Pro, & Valve Index). We have also added experimental support to OpenXR headsets that have Monado drivers (e.g. North Star, OSVR HDK, and PSVR). Some people have gotten the Oculus Rift S to run Simula via OpenHMD ([see here](https://github.com/OpenHMD/OpenHMD/issues/225#issuecomment-638454156)).

# Machine Learning
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/96352527-ad077880-1078-11eb-98b7-da1c0586cf0e.png">
  <br />
</p>

<img src="https://user-images.githubusercontent.com/45159366/105645196-dccfd480-5e4e-11eb-95d1-c5eb560b72fd.jpeg">

**Machine Learning/Deep Learning Frameworks.**

## Learning Resources for ML

[Machine Learning](https://www.ibm.com/cloud/learn/machine-learning) is a branch of artificial intelligence (AI) focused on building apps using algorithms that learn from data models and improve their accuracy over time without needing to be programmed.

[Machine Learning by Stanford University from Coursera](https://www.coursera.org/learn/machine-learning)

[AWS Training and Certification for Machine Learning (ML) Courses](https://aws.amazon.com/training/learning-paths/machine-learning/)

[Machine Learning Scholarship Program for Microsoft Azure from Udacity](https://www.udacity.com/scholarships/machine-learning-scholarship-microsoft-azure)

[Microsoft Certified: Azure Data Scientist Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist)

[Microsoft Certified: Azure AI Engineer Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-ai-engineer)

[Azure Machine Learning training and deployment](https://docs.microsoft.com/en-us/azure/devops/pipelines/targets/azure-machine-learning)

[Learning Machine learning and artificial intelligence from Google Cloud Training](https://cloud.google.com/training/machinelearning-ai)

[Machine Learning Crash Course for Google Cloud](https://developers.google.com/machine-learning/crash-course/)

[JupyterLab](https://jupyterlab.readthedocs.io/)

[Scheduling Jupyter notebooks on Amazon SageMaker ephemeral instances](https://aws.amazon.com/blogs/machine-learning/scheduling-jupyter-notebooks-on-sagemaker-ephemeral-instances/)

[How to run Jupyter Notebooks in your Azure Machine Learning workspace](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks)

[Machine Learning Courses Online from Udemy](https://www.udemy.com/topic/machine-learning/)

[Machine Learning Courses Online from Coursera](https://www.coursera.org/courses?query=machine%20learning&)

[Learn Machine Learning with Online Courses and Classes from edX](https://www.edx.org/learn/machine-learning)

## ML Frameworks, Libraries, and Tools

[TensorFlow](https://www.tensorflow.org) is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

[Keras](https://keras.io) is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.It was developed with a focus on enabling fast experimentation. It is capable of running on top of TensorFlow, Microsoft Cognitive Toolkit, R, Theano, or PlaidML.

[PyTorch](https://pytorch.org) is a library for deep learning on irregular input data such as graphs, point clouds, and manifolds. Primarily developed by Facebook's AI Research lab.

[Amazon SageMaker](https://aws.amazon.com/sagemaker/) is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly. SageMaker removes the heavy lifting from each step of the machine learning process to make it easier to develop high quality models.

[Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/) is a fast and collaborative Apache Spark-based big data analytics service designed for data science and data engineering. Azure Databricks, sets up your Apache Spark environment in minutes, autoscale, and collaborate on shared projects in an interactive workspace. Azure Databricks supports Python, Scala, R, Java, and SQL, as well as data science frameworks and libraries including TensorFlow, PyTorch, and scikit-learn.

[Microsoft Cognitive Toolkit (CNTK)](https://docs.microsoft.com/en-us/cognitive-toolkit/) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.

[Apple CoreML](https://developer.apple.com/documentation/coreml) is a framework that helps integrate machine learning models into your app. Core ML provides a unified representation for all models. Your app uses Core ML APIs and user data to make predictions, and to train or fine-tune models, all on the user's device. A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data.

[Tensorflow_macOS](https://github.com/apple/tensorflow_macos) is a Mac-optimized version of TensorFlow and TensorFlow Addons for macOS 11.0+ accelerated using Apple's ML Compute framework.

[Apache OpenNLP](https://opennlp.apache.org/) is an open-source library for a machine learning based toolkit used in the processing of natural language text. It features an API for use cases like [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition), [Sentence Detection](), [POS(Part-Of-Speech) tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging), [Tokenization](https://en.wikipedia.org/wiki/Tokenization_(data_security)) [Feature extraction](https://en.wikipedia.org/wiki/Feature_extraction), [Chunking](https://en.wikipedia.org/wiki/Chunking_(psychology)), [Parsing](https://en.wikipedia.org/wiki/Parsing), and [Coreference resolution](https://en.wikipedia.org/wiki/Coreference).

[Apache Airflow](https://airflow.apache.org) is an open-source workflow management platform created by the community to programmatically author, schedule and monitor workflows. Install. Principles. Scalable. Airflow has a modular architecture and uses a message queue to orchestrate an arbitrary number of workers. Airflow is ready to scale to infinity.

[Open Neural Network Exchange(ONNX)](https://github.com/onnx) is an open ecosystem that empowers AI developers to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. It defines an extensible computation graph model, as well as definitions of built-in operators and standard data types.

[Apache MXNet](https://mxnet.apache.org/) is a deep learning framework designed for both efficiency and flexibility. It allows you to mix symbolic and imperative programming to maximize efficiency and productivity. At its core, MXNet contains a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on the fly. A graph optimization layer on top of that makes symbolic execution fast and memory efficient. MXNet is portable and lightweight, scaling effectively to multiple GPUs and multiple machines. Support for Python, R, Julia, Scala, Go, Javascript and more.

[AutoGluon](https://autogluon.mxnet.io/index.html) is toolkit for Deep learning that automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. With just a few lines of code, you can train and deploy high-accuracy deep learning models on tabular, image, and text data.

[Anaconda](https://www.anaconda.com/) is a very popular Data Science platform for machine learning and deep learning that enables users to develop models, train them, and deploy them.

[PlaidML](https://github.com/plaidml/plaidml) is an advanced and portable tensor compiler for enabling deep learning on laptops, embedded devices, or other devices where the available computing hardware is not well supported or the available software stack contains unpalatable license restrictions.

[OpenCV](https://opencv.org) is a highly optimized library with focus on real-time computer vision applications. The C++, Python, and Java interfaces support Linux, MacOS, Windows, iOS, and Android.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a Python module for machine learning built on top of SciPy, NumPy, and matplotlib, making it easier to apply robust and simple implementations of many popular machine learning algorithms.

[Weka](https://www.cs.waikato.ac.nz/ml/weka/) is an open source machine learning software that can be accessed through a graphical user interface, standard terminal applications, or a Java API. It is widely used for teaching, research, and industrial applications, contains a plethora of built-in tools for standard machine learning tasks, and additionally gives transparent access to well-known toolboxes such as scikit-learn, R, and Deeplearning4j.

[Caffe](https://github.com/BVLC/caffe) is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR)/The Berkeley Vision and Learning Center (BVLC) and community contributors.

[Theano](https://github.com/Theano/Theano) is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently including tight integration with NumPy.

[nGraph](https://github.com/NervanaSystems/ngraph) is an open source C++ library, compiler and runtime for Deep Learning. The nGraph Compiler aims to accelerate developing AI workloads using any deep learning framework and deploying to a variety of hardware targets.It provides the freedom, performance, and ease-of-use to AI developers.

[NVIDIA cuDNN](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for [deep neural networks](https://developer.nvidia.com/deep-learning). cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers. cuDNN accelerates widely used deep learning frameworks, including [Caffe2](https://caffe2.ai/), [Chainer](https://chainer.org/), [Keras](https://keras.io/), [MATLAB](https://www.mathworks.com/solutions/deep-learning.html), [MxNet](https://mxnet.incubator.apache.org/), [PyTorch](https://pytorch.org/), and [TensorFlow](https://www.tensorflow.org/).

[Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Jupyter is used widely in industries that do data cleaning and transformation, numerical simulation, statistical modeling, data visualization, data science, and machine learning.

[Apache Spark](https://spark.apache.org/) is a unified analytics engine for large-scale data processing. It provides high-level APIs in Scala, Java, Python, and R, and an optimized engine that supports general computation graphs for data analysis. It also supports a rich set of higher-level tools including Spark SQL for SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for stream processing.

[Apache Spark Connector for SQL Server and Azure SQL](https://github.com/microsoft/sql-spark-connector) is a high-performance connector that enables you to use transactional data in big data analytics and persists results for ad-hoc queries or reporting. The connector allows you to use any SQL database, on-premises or in the cloud, as an input data source or output data sink for Spark jobs.

[Apache PredictionIO](https://predictionio.apache.org/) is an open source machine learning framework for developers, data scientists, and end users. It supports event collection, deployment of algorithms, evaluation, querying predictive results via REST APIs. It is based on scalable open source services like Hadoop, HBase (and other DBs), Elasticsearch, Spark and implements what is called a Lambda Architecture.

[Cluster Manager for Apache Kafka(CMAK)](https://github.com/yahoo/CMAK) is a tool for managing [Apache Kafka](https://kafka.apache.org/) clusters.

[BigDL](https://bigdl-project.github.io/) is a distributed deep learning library for Apache Spark. With BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.

[Eclipse Deeplearning4J (DL4J)](https://deeplearning4j.konduit.ai/) is a set of projects intended to support all the needs of a JVM-based(Scala, Kotlin, Clojure, and Groovy) deep learning application. This means starting with the raw data, loading and preprocessing it from wherever and whatever format it is in to building and tuning a wide variety of simple and complex deep learning networks.

[Tensorman](https://github.com/pop-os/tensorman) is a utility for easy management of Tensorflow containers by developed by [System76]( https://system76.com).Tensorman allows Tensorflow to operate in an isolated environment that is contained from the rest of the system. This virtual environment can operate independent of the base system, allowing you to use any version of Tensorflow on any version of a Linux distribution that supports the Docker runtime.

[Numba](https://github.com/numba/numba) is an open source, NumPy-aware optimizing compiler for Python sponsored by Anaconda, Inc. It uses the LLVM compiler project to generate machine code from Python syntax. Numba can compile a large subset of numerically-focused Python, including many NumPy functions. Additionally, Numba has support for automatic parallelization of loops, generation of GPU-accelerated code, and creation of ufuncs and C callbacks.

[Chainer](https://chainer.org/) is a Python-based deep learning framework aiming at flexibility. It provides automatic differentiation APIs based on the define-by-run approach (dynamic computational graphs) as well as object-oriented high-level APIs to build and train neural networks. It also supports CUDA/cuDNN using [CuPy](https://github.com/cupy/cupy) for high performance training and inference.

[XGBoost](https://xgboost.readthedocs.io/) is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. It supports distributed training on multiple machines, including AWS, GCE, Azure, and Yarn clusters. Also, it can be integrated with Flink, Spark and other cloud dataflow systems.

[cuML](https://github.com/rapidsai/cuml) is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects. cuML enables data scientists, researchers, and software engineers to run traditional tabular ML tasks on GPUs without going into the details of CUDA programming. In most cases, cuML's Python API matches the API from scikit-learn.

# Python Development
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/93133273-ce490380-f68b-11ea-81d0-7f6a3debe6c0.png">
  <br />
</p>

## Python Learning Resources

[Python](https://www.python.org) is an interpreted, high-level programming language. Python is used heavily in the fields of Data Science and Machine Learning.

[Python Developer’s Guide](https://devguide.python.org) is a comprehensive resource for contributing to Python – for both new and experienced contributors. It is maintained by the same community that maintains Python.

[Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python) is an introduction to developing Azure Functions using Python. The content below assumes that you've already read the [Azure Functions developers guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference).

[CheckiO](https://checkio.org/) is a programming learning platform and a gamified website that teaches Python through solving code challenges and competing for the most elegant and creative solutions.

[Python Institute](https://pythoninstitute.org)

[PCEP – Certified Entry-Level Python Programmer certification](https://pythoninstitute.org/pcep-certification-entry-level/)

[PCAP – Certified Associate in Python Programming certification](https://pythoninstitute.org/pcap-certification-associate/)

[PCPP – Certified Professional in Python Programming 1 certification](https://pythoninstitute.org/pcpp-certification-professional/)

[PCPP – Certified Professional in Python Programming 2](https://pythoninstitute.org/pcpp-certification-professional/)

[MTA: Introduction to Programming Using Python Certification](https://docs.microsoft.com/en-us/learn/certifications/mta-introduction-to-programming-using-python)

[Getting Started with Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)

[Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)

[Google's Python Education Class](https://developers.google.com/edu/python/)

[Real Python](https://realpython.com)

[The Python Open Source Computer Science Degree by Forrest Knight](https://github.com/ForrestKnight/open-source-cs-python)

[Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science)

[Intro to Python by W3schools](https://www.w3schools.com/python/python_intro.asp)

[Codecademy's Python 3 course](https://www.codecademy.com/learn/learn-python-3)

[Learn Python with Online Courses and Classes from edX](https://www.edx.org/learn/python)

[Python Courses Online from Coursera](https://www.coursera.org/courses?query=python)

## Python Frameworks, Libraries, and Tools

[Python Package Index (PyPI)](https://pypi.org/) is a repository of software for the Python programming language. PyPI helps you find and install software developed and shared by the Python community.

[PyCharm](https://www.jetbrains.com/pycharm/) is the best IDE I've ever used. With PyCharm, you can access the command line, connect to a database, create a virtual environment, and manage your version control system all in one place, saving time by avoiding constantly switching between windows.

[Python Tools for Visual Studio(PTVS)](https://microsoft.github.io/PTVS/) is a free, open source plugin that turns Visual Studio into a Python IDE. It supports editing, browsing, IntelliSense, mixed Python/C++ debugging, remote Linux/MacOS debugging, profiling, IPython, and web development with Django and other frameworks.

[Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

[Flask](https://flask.palletsprojects.com/) is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

[Web2py](http://web2py.com/) is an open-source web application framework written in Python allowing allows web developers to program dynamic web content. One web2py instance can run multiple web sites using different databases.

[AWS Chalice](https://github.com/aws/chalice) is a framework for writing serverless apps in python. It allows you to quickly create and deploy applications that use AWS Lambda.

[Tornado](https://www.tornadoweb.org/) is a Python web framework and asynchronous networking library. Tornado uses a non-blocking network I/O, which can scale to tens of thousands of open connections.

[HTTPie](https://github.com/httpie/httpie) is a command line HTTP client that makes CLI interaction with web services as easy as possible. HTTPie is designed for testing, debugging, and generally interacting with APIs & HTTP servers.

[Scrapy](https://scrapy.org/) is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

[Sentry](https://sentry.io/) is a service that helps you monitor and fix crashes in realtime. The server is in Python, but it contains a full API for sending events from any language, in any application.

[Pipenv](https://github.com/pypa/pipenv) is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

[Python Fire](https://github.com/google/python-fire) is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.

[Bottle](https://github.com/bottlepy/bottle) is a fast, simple and lightweight [WSGI](https://www.wsgi.org/) micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the [Python Standard Library](https://docs.python.org/library/).

[CherryPy](https://cherrypy.org) is a minimalist Python object-oriented HTTP web framework.

[Sanic](https://github.com/huge-success/sanic) is a Python 3.6+ web server and web framework that's written to go fast.

[Pyramid](https://trypyramid.com) is a small and fast open source Python web framework. It makes real-world web application development and deployment more fun and more productive.

[TurboGears](https://turbogears.org) is a hybrid web framework able to act both as a Full Stack framework or as a Microframework.

[Falcon](https://falconframework.org/) is a reliable, high-performance Python web framework for building large-scale app backends and microservices with support for MongoDB, Pluggable Applications and autogenerated Admin.

[Neural Network Intelligence(NNI)](https://github.com/microsoft/nni) is an open source AutoML toolkit for automate machine learning lifecycle, including [Feature Engineering](https://github.com/microsoft/nni/blob/master/docs/en_US/FeatureEngineering/Overview.md), [Neural Architecture Search](https://github.com/microsoft/nni/blob/master/docs/en_US/NAS/Overview.md), [Model Compression](https://github.com/microsoft/nni/blob/master/docs/en_US/Compressor/Overview.md) and [Hyperparameter Tuning](https://github.com/microsoft/nni/blob/master/docs/en_US/Tuner/BuiltinTuner.md).

[Dash](https://plotly.com/dash) is a popular Python framework for building ML & data science web apps for Python, R, Julia, and Jupyter.

[Luigi](https://github.com/spotify/luigi) is a Python module that helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization etc. It also comes with Hadoop support built-in.

[Locust](https://github.com/locustio/locust) is an easy to use, scriptable and scalable performance testing tool.

[spaCy](https://github.com/explosion/spaCy) is a library for advanced Natural Language Processing in Python and Cython.

[NumPy](https://www.numpy.org/) is the fundamental package needed for scientific computing with Python.

[Pillow](https://python-pillow.org/) is a friendly PIL(Python Imaging Library) fork.

[IPython](https://ipython.org/) is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers enhanced introspection, rich media, additional shell syntax, tab completion, and rich history.

[GraphLab Create](https://turi.com/) is a Python library, backed by a C++ engine, for quickly building large-scale, high-performance machine learning models.

[Pandas](https://pandas.pydata.org/) is a fast, powerful, and easy to use open source data structrures, data analysis and manipulation tool, built on top of the Python programming language.

[PuLP](https://coin-or.github.io/pulp/) is an Linear Programming modeler written in python. PuLP can generate LP files and call on use highly optimized solvers, GLPK, COIN CLP/CBC, CPLEX, and GUROBI, to solve these linear problems.

[Matplotlib](https://matplotlib.org/) is a 2D plotting library for creating static, animated, and interactive visualizations in Python. Matplotlib produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms.

[Scikit-Learn](https://scikit-learn.org/stable/index.html) is a simple and efficient tool for data mining and data analysis. It is built on NumPy,SciPy, and mathplotlib.

# R Development
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

<p align="center">
 <img src="https://user-images.githubusercontent.com/45159366/126396985-130c91c7-9db4-4b74-90f8-d11c1876fdd4.png">
  <br />
</p>

## R Learning Resources

[R](https://www.r-project.org/) is an open source software environment for statistical computing and graphics. It compiles and runs on a wide variety of  platforms such as Windows and MacOS.

[An Introduction to R](https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf)

[Google's R Style Guide](https://google.github.io/styleguide/Rguide.html)

[R developer's guide to Azure](https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/r-developers-guide)

[Running R at Scale on Google Compute Engine](https://cloud.google.com/solutions/running-r-at-scale)

[Running R on AWS](https://aws.amazon.com/blogs/big-data/running-r-on-aws/)

[RStudio Server Pro for AWS](https://aws.amazon.com/marketplace/pp/RStudio-RStudio-Server-Pro-for-AWS/B06W2G9PRY)

[Learn R by Codecademy](https://www.codecademy.com/learn/learn-r)

[Learn R Programming with Online Courses and Lessons by edX](https://www.edx.org/learn/r-programming)

[R Language Courses by Coursera](https://www.coursera.org/courses?query=r%20language)

[Learn R For Data Science by Udacity](https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118)

## R Tools, Libraries, and Frameworks

[RStudio](https://rstudio.com/) is an integrated development environment for R and Python, with a console, syntax-highlighting editor that supports direct code execution, and tools for plotting, history, debugging and workspace management.

[Shiny](https://shiny.rstudio.com/) is a newer package from RStudio that makes it incredibly easy to build interactive web applications with R.

[Rmarkdown ](https://rmarkdown.rstudio.com/) is a package helps you create dynamic analysis documents that combine code, rendered output (such as figures), and prose.

[Rplugin](https://github.com/JetBrains/Rplugin) is R Language supported plugin for the IntelliJ IDE.

[Plotly](https://plotly-r.com/) is an R package for creating interactive web graphics via the open source JavaScript graphing library [plotly.js](https://github.com/plotly/plotly.js).

[Metaflow](https://metaflow.org/) is a Python/R library that helps scientists and engineers build and manage real-life data science projects. Metaflow was originally developed at Netflix to boost productivity of data scientists who work on a wide variety of projects from classical statistics to state-of-the-art deep learning.

[Prophet](https://facebook.github.io/prophet) is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data.

[LightGBM](https://lightgbm.readthedocs.io/) is a gradient boosting framework that uses tree based learning algorithms, used for ranking, classification and many other machine learning tasks.

[Dash](https://plotly.com/dash) is a Python framework for building analytical web applications in Python, R, Julia, and Jupyter.

[MLR](https://mlr.mlr-org.com/) is Machine Learning in R.

[ML workspace](https://github.com/ml-tooling/ml-workspace) is an all-in-one web-based IDE specialized for machine learning and data science. It is simple to deploy and gets you started within minutes to productively built ML solutions on your own machines. ML workspace is the ultimate tool for developers preloaded with a variety of popular data science libraries (Tensorflow, PyTorch, Keras, and MXnet) and dev tools (Jupyter, VS Code, and Tensorboard) perfectly configured, optimized, and integrated.

[CatBoost](https://catboost.ai/) is a fast, scalable, high performance Gradient Boosting on Decision Trees library, used for ranking, classification, regression and other machine learning tasks for Python, R, Java, C++. Supports computation on CPU and GPU.

[Plumber](https://www.rplumber.io/) is a tool that allows you to create a web API by merely decorating your existing R source code with special comments.

[Drake](https://docs.ropensci.org/drake) is an R-focused pipeline toolkit for reproducibility and high-performance computing.

[DiagrammeR](https://visualizers.co/diagrammer/) is a package you can create, modify, analyze, and visualize network graph diagrams. The output can be incorporated into R Markdown documents, integrated with Shiny web apps, converted to other graph formats, or exported as image files.

[Knitr](https://yihui.org/knitr/) is a general-purpose literate programming engine in R, with lightweight API's designed to give users full control of the output without heavy coding work.

[Broom](https://broom.tidymodels.org/) is a tool that converts statistical analysis objects from R into tidy format.


## Contribute

- [x] If would you like to contribute to this guide simply make a [Pull Request](https://github.com/mikeroyal/Photogrammetry-Guide/pulls).


## License
[Back to the Top](https://github.com/mikeroyal/Photogrammetry-Guide#table-of-contents)

Distributed under the [Creative Commons Attribution 4.0 International (CC BY 4.0) Public License](https://creativecommons.org/licenses/by/4.0/).
