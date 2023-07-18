# LOST AND FOUND
Welcome one, welcome all, to the lost and found challenge, set by me!
For more info on the Scenario, please see [Scenario.txt](Scenario.txt)

### How To:
Firstly, please download this project! Yes, in its entirety! It may be big, so, bare with it. big_data has been fully sanitised to be only txt files, so dont worry, powers that be!

Next, you will want to pick some data at random from [big_data](big_data/). Copy the folders that you have selected (such as [ht](big_data/ht/) for example) into [chosen_data](chosen_data/). All files in [chosen_data](chosen_data/) will be processed!

After this, run [dataCreation.py](dataCreation.py). This can be done with
`sh
python dataCreation.py
`
(or otherwise). 

This will generate alot of data in [input_data](input_data/). It might be worth looking at this first before you start! (hint hint)

Finally, get familiar with what is written in [answerChecker.py](answerChecker.py), and use this class to verify your answers that you may find! Work together, work collaboratively, more challenges may be added ontop of this too!


Note: [useful.py](useful.py) was for my use when filtering big_data. I left it in as an example of how python can be used to automate large, repetative tasks with ease. You can ignore this file completely. 


### Rules
Yuck, rules, ikr. But they are important!
- Be sensible with the amount of data processed! big_data has (give or take) the entire UK as a terrain map. This can get big should it all be processed! It will also take ages (the algorithm has not been optimised on purpose!) Please be sensible and only process a resonable amount of data. Each file that is processed will create 5 bits of input_data. Please do not abuse this!
- You must work together! This is a team-buidling activity, after all! 
- Please do not edit dataCreation.py, or AnswerChecker.py. These are operational files (that being said, they may contain errors! If you suspect something may be up, you are free to investigate.)
- Please do not abuse / spam the answer checker system. 
- You may read through dataCreation.py for a better idea of what is going on 

### Where do i code?
You will find a file called main.py. Please use this. A basic template has been set up to get you started. 

### How to install the required dependancies
Run the below in a suitable python terminal.
`sh
pip install matplotlib numpy
`

### Credits:
Map data found from [Here](https://osdatahub.os.uk/downloads/open).
