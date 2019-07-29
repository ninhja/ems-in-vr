# Augmenting VR with Electrical Muscle Stimulation (EMS) as Haptic & Force Feedback

This repo documents my explorations in using electrical muscle stimulation (EMS) to provide tactile and force feedback in an intensive care unit VR environment to increase the sense of presence and immersion.

[My Day-to-Day Process Notes (but skip this and read below... I'm just leaving it here for my own reference)](https://docs.google.com/document/d/1RLxw7XNduukD_50_s6lb3dYKiTGEtaLbcdvorFLF1EQ/edit?usp=sharing)

## 1. Tools

#### Hardware
[Medical-grade EMS device](https://tenswelt.de/products/tns-sm-2-mf-tens-reizstromgeraet-mit-burst-und-modulation) 

  - I used this analog device to generate the electrical signals. It has 2 channels, which means you can use it to control at most 2 muscles. It requires a 9 volt battery.

[50 mm Self-adhesive electrodes](https://tenswelt.de/pages/produkte/collections/elektroden-and-zubehoer/products/stimex-klebeelektroden-50-x-50-mm-selbstklebeelektroden-fuer-tens-und-ems)

  - These come off easily, so it's handy to use medical tape, rubber bands, velcro straps, or whatever you have on hand  to keep the electrodes secured on the skin. 

[openEMSstim hardware module](http://plopes.org/ems/)

  - For communicating between the EMS device and Unity, I used Pedro Lopes' awesome open-hardware EMS module called openEMSstim. To learn how to use it, check out [the openEMSstim github repo](https://github.com/PedroLopes/openEMSstim) for the full documentation.
  
  
#### Software 
  Unity and [HTC Vive Hand Tracking SDK](https://developer.viveport.com/documents/sdk/en/vivehandtracking_index.html?_ga=2.71670870.493605801.1564407317-1284242289.1562595620) (which only works with the HTC Vive).
  

## 2. Basics of Electrical Muscle Stimulation (EMS) 
In a nutshell, the reason why EMS works is because the artificial electrical signal of EMS mimics the electrical impulses that occur naturally in human bodies, as a result of the central nervous system firing action potentials that cause muscles to contract. The electrical impulses are generated by the EMS device and get delivered to the muscle through electrode pads placed on the skin above the muscle. 

Before you can do anything with EMS, first you need to learn how to safely use your EMS device. 

There are many ways that affect how the electrical signal feels, such as the following:
1. Electrode placement (where the electrodes are placed on the skin over the muscle, and how far away they are from each other)
2. The parameters for generating the electrical signal
3. Adhesiveness and size of the electrodes you use
4. The individual's skin (sweat increases conductivity, dry skin decreases conductivity, and hair can sometimes interfere with the signal) 

I think one aspect of EMS that's unavoidable (but perhaps I am wrong?) is that the user will feel some muscle fatigue after using EMS. This is especially true if using EMS for longer periods of time, or if the EMS is not properly calibrated (i.e. bad electrode placement, electrodes that lost their stickiness, etc). For that reason, it's important to properly calibrate the signal to avoid discomfort/muscle fatigue as much as possible. 

Pedro Lopez made a great calibration tutorial, which you can read in step-by-step detail [here](https://github.com/PedroLopes/openEMSstim/blob/master/start-here-tutorials/1.getting_started_step_by_step.md), and he also made a tutorial video that you can watch [here.](http://plopes.org/ems/#testingEMSmachine) 

#### Placing Electrodes
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

#### Calibrating the Parameters of the Electrical Signal
I did a lot of experimentation with the parameters of the electrical signal in order to actuate muscles while minimizing discomfort and muscle fatigue. With the TNS SM 2 analog EMS device that I used, I can control the intensity (amplitude) of both channels, and also the frequency in Hertz.  

Here are some tips that I learned for electrical signal parameters: 
1. I found that the best frequency for me was around 50 Hz. I found that higher frequencies beyond 50 Hz didn't change the strength of the muscle actuation at all, but I felt more muscle fatigue after using EMS with higher frequencies. 
2. I learned the following from [this webpage](https://tens-ems.com/en/ems/device-settings/(https://tens-ems.com/en/ems/device-settings/):
  - “Low frequencies (no higher than about 18 Hz) will mainly activate the slower reacting red muscle fibers. Power and endurance athletes will thus benefit from electrical muscle stimulation in this frequency range to build up muscle. When applied, it will cause a distinct contraction of the muscle.”
  - “Higher frequencies between 30 and 50 Hz stimulate the fast contracting white muscle fibers.”
  - “With frequencies of over 50 Hz, the muscle is deliberately overtaxed and can thus be forced into muscle hypertrophy (muscle build-up). To avoid overtraining, the interval between the sessions must be correctly chosen so that the muscle has enough time to regenerate.” 
3. Frequencies that are around 30 Hz or lower feel noticeably different. I can more palpably slower vibrations and ticks. 
4. The right intensity setting changes from individual to individual, and it's also different every time for the same individual, because of varying skin conductivity and size/location/depth of the muscle. Skin conductivity is affected by the amount of sweat and hair on the skin. So it's important to carefully calibrate the right intensity settomg every time you use EMS. Start low and slow, and gradually increase the intensity until you achieve a pain-free muscle actuation. 
5. Read more from Pedro Lopes' [tips and tricks doc here](https://github.com/PedroLopes/openEMSstim/blob/master/start-here-tutorials/4.exploring_ems_settings_and_parameters.md).

## 3. Using EMS in Unity 

The openEMSstim module communicates with Unity via Serial USB communication. You can send EMS commands from Unity to the openEMSstim module using the openEMSstim communication protocol, which you can [read about here.](https://github.com/PedroLopes/openEMSstim/blob/master/start-here-tutorials/3.software_guide.md)

#### EMS Signal Calibration in Unity
Before you start using EMS in your VR environment, it's helpful to find the right parameters first with this simple calibration GUI that I created in Unity, which works for up to 2 EMS channels. You can find it in this repo as a file called EMS_Calibration.unitypackage. Import the package into Unity and play the scene.

Before you press any button on the GUI to send commands to the openEMSstim hardware module, it takes a bit of time for Unity to establish a working connection with openEMSstim. At the top of the screen, you'll see a time counter that tells you how many seconds passed since the scene started. Wait about 10 seconds after starting until you starting sending EMS commands. Then you can start clicking on buttons on the GUI to trigger an EMS signal for the corresponding channel and intensity for 500 ms. 

You can change the EMS commands that are mapped to the buttons on the GUI by changing EMS command variables in the Manager.cs script. You can also look at the GM object in the project hierarchy, and then change the variables under the Manager script component in Inspector.  

#### Using EMS in the ICU Scene in Unity
Like with the Calibration GUI explained above, you have to wait about 10 seconds after pressing play on the ICU scene until EMS starts to work. 

I used 2 EMS channels to actuate 2 muscles on one arm: one channel on the triceps and the other channel on the palm extensor on the forearm. When the player touches any hard object, they get a gentle actuation of the palm extensor muscle, which extends the palm backwards to simulate the impact of the hand colliding with a surface. When the player holds an object (in this scene, the player can hold the Medicine Carousel object) they feel vibration haptic feedback on their triceps to simulate feeling the weight of the object.

EMS haptic and force feedback gets triggered in the Unity scene when the player enters a trigger collider attached to an object. That object contains a script that communicates with the attached openEMSstim object (it's called openEMSstim_container in the project hierarchy). 

There are two different EMS-enabling scripts that I used. One is called EMS_HardSurfaces.cs, which triggers gentle actuation of the palm flexor when the player touches a surface with their hand. Another is called EMS_GrabObject.cs, which triggers gentle vibration of the triceps when the player holds an object. When the player enters the object's trigger collider, OnTriggerEnter gets called, which sends the stimulation command to the openEMSstim module.

I designed 4 types of interactions with EMS haptic/force feedback in this ICU environment. 
1. You can walk around the ICU room and touch things, triggering a slight actuation of the palm flexor. 
2. There are 5 different machines around the room that make loud annoying alarm noises, and you can tell if they're making an alarm if the machine's screen or buttons are glowing red. Touch the machine and the alarm will turn off, and the screen or buttons will turn green. Touch it again, and the alarm will turn back on and so will the red signals. Touching the machine will trigger a slight actuation of the palm flexor.
3. There's a person on the bed. Touching the person will stop their coughing and make them sleep instead. Touching them will trigger a slight actuation of the palm flexor.
4. On top of the ventilator (which is the machine to the left of the bed), there is a medicine carousel, which is the small white disc-shaped object. You can pick it up by closing your hand into a fist, then move it towards the medicine carousel until it moves into your hand. As long as you keep holding your hand into a closed fist, you'll continue to hold the object, and you'll get a gentle vibration on your tricep muscle to simulate feeling the weight of the object. As soon as you open your hand and move it away from the object, the object will drop and the tricep muscle stimulation will end. 
  - Note: your hand displayed in VR will turn blue to signal that Unity recognizes your hand gesture as a closed fist.

#### Hands-Free Interaction in VR
For interacting with the VR environment, I decided not to use the handheld controllers that come with the HTC Vive. This is because I wanted to actuate the palm flexor muscle, and it would be difficult to hold onto the handheld controller when actuating that muscle. I also thought that having hands-free interaction would make interacting with the VR environment feel a lot more natural and less clunky. 

You can find the documentation for the [HTC Vive Hand Tracking SDK here.](https://developer.vive.com/resources/knowledgebase/vive-hand-tracking-sdk/). The tracking can be a bit laggy, and the thumb looks weird most of the time, but for the most part it works pretty well for our purposes. 
- An important thing to note is that it works a lot better if the wrist is visible and not covered by clothing. 
- The color of the hands changes depending on the gesture. The Hand Tracking SDK can recognize 5 different gestures. In the ICU Unity scene, the only notable gesture to remember is that the hand turns blue when it's a fist. 


