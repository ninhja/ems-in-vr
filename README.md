# ems-in-vr
## augmenting immersive VR with electrical muscle stimulation (EMS) as haptic/force feedback

This repo documents my explorations in using electrical muscle stimulation (EMS) to provide tactile and force feedback in an intensive care unit VR environment to increase the sense of presence and immersion.

[Day-to-Day Process Notes](https://docs.google.com/document/d/1RLxw7XNduukD_50_s6lb3dYKiTGEtaLbcdvorFLF1EQ/edit?usp=sharing)

### EMS Hardware Materials
Below is a list of all of the materials I used in the making of this project. 

[This is the medical-grade EMS device](https://tenswelt.de/products/tns-sm-2-mf-tens-reizstromgeraet-mit-burst-und-modulation) that I used to generate the electrical signals. It has 2 channels, which means you can use it to control at most 2 muscles. It is also an analog device that requires a 9 volt battery. 

[These are the self-adhesive electrodes that I used.](https://tenswelt.de/pages/produkte/collections/elektroden-and-zubehoer/products/stimex-klebeelektroden-50-x-50-mm-selbstklebeelektroden-fuer-tens-und-ems). Each channel on the EMS device requires 2 electrodes which you stick on your skin over the muscle you want to actuate or send haptic feedback to. The larger the size of the electrode, the more the electrical signal gets distributed throughout the muscle and surrounding skin/tissue. Smaller electrodes might give you a bit more precision in targeting a specific muscle, but it may be more difficult to find the right electrode placement in calibration. I used 50mm electrodes, which are on the larger end, which gives me more flexibility and leeway in finding electrode placements that painlessly actuate muscles (but they may be too large to precisely actuate specific muscles that are smaller, such as muscles for individual fingers.)

For communicating between the EMS device and Unity, I used Pedro Lopes' awesome open-hardware EMS module called openEMSstim. To learn how to use it, check out [the openEMSstim github repo](https://github.com/PedroLopes/openEMSstim) for the full documentation. 

### 1. Familiarize yourself with electrical muscle stimulation (EMS) 
Before you can do anything with EMS, first you need to learn how to safely use your EMS device. 

Here are some tips I learned for safe electrode placement: 
It’s generally safer to put the electrodes on the right side of the body because it’s further away from the heart. 
When placing 2 electrodes for a single channel, always put the 2 electrodes within a few centimeters away from one another, and always on the same side of the body (otherwise the electric signal will go through the heart, which you don’t want.)
Read more about [what NOT to do with using an EMS device here](https://github.com/PedroLopes/openEMSstim/blob/master/start-here-tutorials/0.WhatNotToDo.md). 


