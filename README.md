# Augmenting VR with Electrical Muscle Stimulation (EMS) as Haptic & Force Feedback

This repo documents my explorations in using electrical muscle stimulation (EMS) to provide tactile and force feedback in an intensive care unit VR environment to increase the sense of presence and immersion.

[My Day-to-Day Process Notes (but skip this and read below... I'm just leaving it here for my own reference)](https://docs.google.com/document/d/1RLxw7XNduukD_50_s6lb3dYKiTGEtaLbcdvorFLF1EQ/edit?usp=sharing)

## 1. EMS hardware materials
Below is a list of all of the materials I used in the making of this project. 

[Medical-grade EMS device](https://tenswelt.de/products/tns-sm-2-mf-tens-reizstromgeraet-mit-burst-und-modulation) 
I used this analog device to generate the electrical signals. It has 2 channels, which means you can use it to control at most 2 muscles. It requires a 9 volt battery. 

[Self-adhesive electrodes](https://tenswelt.de/pages/produkte/collections/elektroden-and-zubehoer/products/stimex-klebeelektroden-50-x-50-mm-selbstklebeelektroden-fuer-tens-und-ems). 

[openEMSstim hardware module](http://plopes.org/ems/)
For communicating between the EMS device and Unity, I used Pedro Lopes' awesome open-hardware EMS module called openEMSstim. To learn how to use it, check out [the openEMSstim github repo](https://github.com/PedroLopes/openEMSstim) for the full documentation. 

## 2. Familiarize yourself with electrical muscle stimulation (EMS) 
Before you can do anything with EMS, first you need to learn how to safely use your EMS device. 

There are many ways that affect how the electrical signal feels, such as the following:
1. Electrode placement (where the electrodes are placed on the skin over the muscle, and how far away they are from each other)
2. The parameters for generating the electrical signal
3. Adhesiveness and size of the electrodes you use
4. The individual's skin (sweat increases conductivity, dry skin decreases conductivity, and hair can sometimes interfere with the signal) 

### Placing electrodes
Here are some tips I learned for electrode placement: 
1. It’s generally safer to put the electrodes on the right side of the body because it’s further away from the heart. 
2. When placing 2 electrodes for a single channel, always put the 2 electrodes within a few centimeters away from one another, and always on the same side of the body (otherwise the electric signal will go through the heart, which you don’t want.)
3. I found that the muscle actuation worked best for me when there was a distance of about 1-2 centimeters between the two electrodes. However it is always relative to the muscle and individual's anatomy, so play around with it and find what works best for you. The closer together the electrodes are, the stronger the electric signal will feel on the skin. The farther away they are from each other, the more muscle/tissue the electric signal has to travel through, so the signal will get weaker. 
4. If you find that you're feeling pain or discomfort without getting a muscle contraction, then the electrode placement is most likely wrong. Adjust the electrodes until you get pain-free actuation. 
5. Read more about [what NOT to do with using an EMS device here](https://github.com/PedroLopes/openEMSstim/blob/master/start-here-tutorials/0.WhatNotToDo.md). 
6. Each channel on the EMS device requires 2 electrodes which you stick on your skin over the muscle you want to actuate or send haptic feedback to. The larger the size of the electrode, the more the electrical signal gets distributed throughout the muscle and surrounding skin/tissue. Smaller electrodes might give you a bit more precision in targeting a specific muscle, but it may be more difficult to find the right electrode placement in calibration. I used 50mm electrodes, which are on the larger end, which gives me more flexibility and leeway in finding electrode placements that painlessly actuate muscles (but they may be too large to precisely actuate specific muscles that are smaller, such as muscles for individual fingers.)
7. Familiarize yourself with human anatomy! You can't actuate muscles if you don't know where the muscles are. Here are some links that helped me figure out where the muscles are:
- [Pad placement charts](https://www.toneamatic.com/pages/pad-placement)
- [Pad placement tips/explanation (plus videos on electrode placement)](http://www.globususa.com/electrode-placement-explained) 
- [More tips](http://proffessa.co.za/articles/electrode-placements/)

### Finding the right parameters for the electrical signal 
I did a lot of experimentation with the parameters of the electrical signal. Basically, the reason why EMS works is because the artificial electrical signal of EMS mimics the electrical impulses that occur naturally in human bodies to move muscles. With the TNS SM 2 analog EMS device that I used, I can control the intensity (amplitude) of both channels, and also the frequency in Hertz.  

Here are some tips that I learned for electrical signal parameters: 
1. I found that the best frequency for me was around 50 Hz. I found that higher frequencies beyond 50 Hz didn't change the strength of the muscle actuation at all, but I felt more muscle fatigue the higher the frequency. 
2. I learned this from [this webpage]https://tens-ems.com/en/ems/device-settings/(https://tens-ems.com/en/ems/device-settings/):
- “Low frequencies (no higher than about 18 Hz) will mainly activate the slower reacting red muscle fibers. Power and endurance athletes will thus benefit from electrical muscle stimulation in this frequency range to build up muscle. When applied, it will cause a distinct contraction of the muscle.”
- “Higher frequencies between 30 and 50 Hz stimulate the fast contracting white muscle fibers.”
- “With frequencies of over 50 Hz, the muscle is deliberately overtaxed and can thus be forced into muscle hypertrophy (muscle build-up). To avoid overtraining, the interval between the sessions must be correctly chosen so that the muscle has enough time to regenerate.” 
3. Frequencies that are around 30 Hz or lower are noticeably different. I can more palpably feel the vibrations and ticks. 
4. The right intensity setting changes from individual to individual, and it's also different every time for the same individual. Skin conductivity is affected by the amount of sweat and hair, the size of the muscle, etc. So it's important to carefully calibrate the intensity every time you use EMS, starting low and slow and gradually increasing the intensity until you achieve a pain-free muscle actuation. 



Read more from Pedro Lopes' [tips and tricks doc here](https://github.com/PedroLopes/openEMSstim/blob/master/start-here-tutorials/4.exploring_ems_settings_and_parameters.md).


Some links with helpful relevant info that helped me: 
- [EMS in HCI: Challenges and Opportunities in Actuating Human Bodies](https://hci.uni-hannover.de/papers/duente2017Tutorial.pdf)
  - “A study with EMS needs specific treatment of the participants such as clear introduction on the technology and consent forms, which should also address risks and safety information. The participants have to confirm that they have no relevant health issues and agree to get electrodes attached to their bodies by the instructor. After that there should be a step by step introduction to EMS to allow the participant to get used to the sensation. For reproducibility of the user study, EMS parameters should be reported such as frequency, pulse width, voltage, and current.” 


