# EAPS-Research

I use this repository to show the work I accomplished whilst doing research for Professor Lei Wang of Purdue EAPS. This will include some amount of code, as well as resources and presentations I made/used.

Throughout this research, I worked with the MACDA and EMARS data sets. The MACDA Data which stands for Mars Analysis Correction Data Assimilation is a reanalysis dataset which covers four years of the martian atmospheric data (MY 24 - MY 27). It is constructed by TES (Thermal Emission Spectrometer) and MGS (Mars Global Surveyor) and is 63 files in total. Each of these files covers 30 Martian sols with each sol spanning 24 Martian hours and data being captured every two hours. This dataset covers a limited number of variables including “co2ice” (surface_frozen_carbon_dioxide_amount), “Ls” ("solar_longitude), latitude and longitude, etc

You can find my AGU profile here: https://agu.confex.com/agu/fm22/meetingapp.cgi/Person/1197083

File Information:
+ Mars Climate Project guide:
+ 


Notes for paper:
- a particular way to help you extract the dominant mode of the system. it's a way to compress the data
What to say:
- Let's quickly go over three important definitions. I'm sure we've heard these many times over, but just in case someone forgot, we'll quickly go over them. Barotropic and Baroclinic
- now, with these three definitions aside, we can just think of barotropic as having no vertical component, while baroclinic has a vertical component.
- Here's a visual. This is actually the ocean, but I think it shows the differences very well.
- There's more to talk about with these, like how a baroclinic atmosphere come to exist, but since that isn't the focus of the paper, I won't go over it. I'd like to mention that I will be sending the slides in the slack which will have videos going over barotropic and baroclinic atmospheres.
- So, the main question that the paper proposes is in regards to the importance of annular modes in the martian atmosphere. so we know that annular modes are crucial to the atmosphere here, but is it in mars or titan? Well, the answer is yes! Not just are they vital to understanding the martian and titan atmospheres, but they explain more on those atmospheres than they do for Earth's atmosphere! Which is incredible because Battalio and Lora explain early in their paper that "The importance of annular variability on Mars was previously reported to be minimal".
- one point of confusion that I had here and perhaps Lei could give an answer to this is why Battalio and Lora decided to investigate annular modes in these two atmospheric bodies when it was already thought that there wasn't really much there. they explain that there was a motivation to do so because they thought it would lead to better weather predictions, but what sparked this motivation?
- however, that aside, let's take a look at the annular modes on mars and titan's atmospheres.
- Through an EOF Analysis (which will be briefly discussed in the ‘Methods’ section), it was discovered that annular modes explain most of the variability in the mid to high latitudes during fall and winter seasons (solar longitude of 180°-370° and 10°-190° in the Northern and Southern hemispheres respectively)
- The U-AM has two spatial structures, a dipolar structure, but only in the Northern Heisphere, and a mono-polar structure only in the southern hemisphere. Due to the southern hemisphere's topography varying with latitude, the dipolar structure cannot exist there. This is because a dipolar structure continuously of the jet stream (exactly like on Earth). This dipolar structure explains roughly 20-30 percent of the variability while the mono-polar structure explains slightly more at roughly 25-35 percent of the variability. Nonetheless they have about the same importance.
- Most importantly, even across the two datasets that were used (which we'll also talk about in the 'Methods' section), the spatial locations of the dipolar modes align at 100 Pa (which is roughly 20 km in altitude). This implies that the spatial patterns are robust.
- Like already mentioned, the dipolar U-AM lacks any vertical tilt. In other words, it's barotropic.
- Battalio explains how it's found that the U-AM is a barotropic feature, but to be completely honest, I don't completely understand it and therefore don't feel comfortable speaking on it. It's in page the second paragraph on the left in the second page.
- This U-AM in the martian atmosphere is very similar to the one in Earth's atmosphere. Hence, the dynamics that explain variability on Earth and Mars are similar. Therefore, we can conclude that annular modes are important features of the martian atmosphere as well.
- the Martian U-AM is annular can be calculated by the surface pressure or the zonal mean zonal wind 
- There’s also a baroclinic annular mode identified in the Martian atmosphere which explains the variability of the EKE.
- Named the “zonal-mean EKE (EKE-AM)”, it resembles Earth’s Baroclinic mode.
- This also had multiple spatial patterns. The single monopole spatial pattern, which is also robust across the Northern and southern hemisphere as well as the MACDA and EMARS dataset, explains about 48-65 percent of the Eddy kinetic energy variance during the fall and winter! this is really exciting news because this is more than Earth's mode.
- This could even be used to determine dust events!
-  The EKE-AM is associated with eddy fluxes of momentum
- So with these exciting news that the EKE-AM explains 48-65 percent of eddy kinetic energy, one must think, can we predict dust activity? The answer is yes!
- in the northern hemisphere, which are dust-lifting regions,
dust activity peaks before the EKE-AM, meaning that dust is lifted
by atmospheric waves before the EKE-AM reaches peak intensity
- however, although there are no reanalysis datasets for Titan yet, we do have the general circulation model know as Titan atmospheric model (TAM for short). Using TAM, we Battalio and Lora were able to find evidence of zonal-mean zonal wind and EKE annular modes!
- As a note, I wanted to say that although the model is well-validated, it is at the end of the day just a single model.
- Nevertheless, the U-AM is dipolar, similar to Mars’, but explains more and is stacked vertically. when we saw the pictures of the U-AM on the Mars, we could see that they were actually stacked horizontally.
- most excitingly, this annular mode explains roughly 68 percent of the variance. More than Earth's, and even Mars' annular modes!
- although they are stacked vertically, there's still an annular feature between 30 degrees and 45 degrees North-south
- well what about it's EKE-AM, that is also exciting, and slightly different from Earth's or Mars' modes. The EKE-AM explains 38.5 percent of the southern, and 52 percent of the northern variability with a single center of action at 500 hpa and 60 degrees north south which is shown in figure 5 in c and d.
- however, very interestingly, taken straight from the paper and I quote "the EKE-AM exhibits a vertically stacked dipole of eddy heat fluxes that are poleward at high altitudes and equatorward at the mid-levels. These equatorward eddy heat fluxes indicate that the waves generating the EKE cannot be baroclinic at the mid-levels of the atmosphere". Overmore, the EKE-AM shares some characteristics of both the martian and the earth annular modes.
- We even saw that it was more useful for Mars than for Earth’s (at least, in the context of the EKE-AM).
- Now, onto the methods. And I think this is the last real slide before my references. For Mars, the MACDA and EMARS reanalysis data sets were used. These are the most popular datasets along with OpenMARS. Time on Mars is measured in degrees with aerocentric longitude (also known as solar longitude). So a solar longitude of 0 degrees is the vernal equinox, then summer, then autumn, then finally winter. I'm sure we've heard of these and had used them at least once (especially in the EAPS 520 homework), so I won't go into any more detail. If anyone would like, I do have notes on these datasets along with their variable names, descriptions, and everything else from Panoply so if you'd like to get that information please let me know. It's not difficult to get it just tedious to collect it all.
- As already mentioned, there are not yet any reanalysis datasets for Titan, so TAM was used. According to Battalio and Lora, and I again quote, this time from page 7, "TAM has been thoroughly vetted against numerous observations of Titan, and its simulated circulation has been shown to be robust as well as favourably comparable to other models’ simulations of Titan’s climate. Nevertheless, the Titan analyses described here are of a single model, so should be interpreted with caution".
- Empirical Orthogonal Function (EOF) was used to identify the annular climatic variability within Earth, Mars, and Titan. I'm also not confident in speaking about this as I've yet to understand it fully. However, Thanks to Lei, I am providing notes which is my last reference here on the slides for anyone who wants to look into EOF. I'll also be looking into it in my free time to better understand it and I'll post these slides in the slack :)

- Finally, before ending, I had a question concerning this paper that I don't think was answered. How is the amount of variability explained by an annular mode determined?
