#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3        on October 21, 2020, at 11:36
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
import csv

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
print('_thisDir; ',_thisDir)
# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'EYEswipe'  # from the Builder filename that created this script
expInfo = {'id*': '', 'participant*': '', 'Interested In(Men/Women)*': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['id*'], expName, expInfo['date'])
# #################target csv file at the end of experimet
filename1 = _thisDir + os.sep + u'expInfo/%s_%s_%s' % (expInfo['id*'], expName, expInfo['date'])
csvfile = open(filename1+".csv", "a", newline='')
writer = csv.writer(csvfile)
writer.writerow(["Trial Number", "State", "Device timestamp","Left pupil diameter","Left pupil validity","Right pupil diameter","Right pupil validity", "Rating"])
##########################################
##sexual orientation check
trialImages='menimgUrl.xlsx' if expInfo['Interested In(Men/Women)*'].lower() == 'men' else 'womenimgUrl.xlsx'
print(trialImages)
################################

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir + os.sep +'testScript1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
TODO = visual.TextStim(win=win, name='TODO',
    text='Welcome:\n\nEach picture is preceded by a scramblbed version, focus picture and think about whether you like the person or not, indicate your choice afterwards with a button press.\n\nPress any key to start the trial.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
StartTrialPress = keyboard.Keyboard()

# Initialize components for Routine "Baseline"
BaselineClock = core.Clock()
baselineImage = visual.ImageStim(
    win=win,
    name='baselineImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
import time
import tobii_research as tr
from msvcrt import getch
import sys
from psychopy import data

# ref code used
# http://devtobiipro.azurewebsites.net/tobii.research/python/reference/1.8.0.32-alpha-g5b38a1f5/gaze_data_8py-example.html

# in sec
timer = 2000
# reading per sec
frequency = 10
global_gaze_data = None
# in second
fixation_threshhold = 0.5
# minimum 
fixation_tolerance = 0.0005

imageId = 1

def initTobii():
    current_eye_tracker = tr.find_all_eyetrackers()[0]
    # print(current_eye_tracker)
    return current_eye_tracker


def getTimeStamp():
    return int((time.time() - start_time) * 1000)

def gaze_data_callback(gaze_data):
    global global_gaze_data
    global_gaze_data = gaze_data

start_time = time.time()
eyetracker = initTobii();
eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
print ("tobii inilialized")
print(getTimeStamp())


# Initialize components for Routine "imageShow"
imageShowClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    
# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=['Yes', 'No'], tickHeight=-1)
NextImagePress = keyboard.Keyboard()
RatingText = visual.TextStim(win=win, name='RatingText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
ThanksText = visual.TextStim(win=win, name='ThanksText',
    text='Thank you for participating this experiment.\n\nPlease press any key to finish this trial.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
StopTrialPress = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
# update component parameters for each repeat
StartTrialPress.keys = []
StartTrialPress.rt = []
# keep track of which components have finished
InstructionComponents = [TODO, StartTrialPress]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TODO* updates
    if TODO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TODO.frameNStart = frameN  # exact frame index
        TODO.tStart = t  # local t and not account for scr refresh
        TODO.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TODO, 'tStartRefresh')  # time at next scr refresh
        TODO.setAutoDraw(True)
    
    # *StartTrialPress* updates
    waitOnFlip = False
    if StartTrialPress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        StartTrialPress.frameNStart = frameN  # exact frame index
        StartTrialPress.tStart = t  # local t and not account for scr refresh
        StartTrialPress.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(StartTrialPress, 'tStartRefresh')  # time at next scr refresh
        StartTrialPress.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(StartTrialPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if StartTrialPress.status == STARTED and not waitOnFlip:
        theseKeys = StartTrialPress.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TODO.started', TODO.tStartRefresh)
thisExp.addData('TODO.stopped', TODO.tStopRefresh)
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(trialImages),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))
#####looop is started
counter = 1
for thisTrial in trials:
    currentLoop = trials
    
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Baseline"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    baselineImage.setImage(Scramble)
    
    start_time = time.time()
    allGazeData = []
    csvGaze=[]
    # keep track of which components have finished
    BaselineComponents = [baselineImage]
    for thisComponent in BaselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BaselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BaselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baselineImage* updates
        if baselineImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baselineImage.frameNStart = frameN  # exact frame index
            baselineImage.tStart = t  # local t and not account for scr refresh
            baselineImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baselineImage, 'tStartRefresh')  # time at next scr refresh
            baselineImage.setAutoDraw(True)
        if baselineImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baselineImage.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                baselineImage.tStop = t  # not accounting for scr refresh
                baselineImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(baselineImage, 'tStopRefresh')  # time at next scr refresh
                baselineImage.setAutoDraw(False)
        print(global_gaze_data)
        time.sleep(1/frequency)
        print(getTimeStamp())
        
        allGazeData.append(global_gaze_data)
        ###################collecting data for csv final reading(baseline)
        csvGaze.append(['Trial'+str(counter),'baseline',global_gaze_data['device_time_stamp'],global_gaze_data['left_pupil_diameter'],global_gaze_data['left_pupil_validity'],global_gaze_data['right_pupil_diameter'],global_gaze_data['right_pupil_validity']])
        
       
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BaselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Baseline"-------
    for thisComponent in BaselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('baselineImage.started', baselineImage.tStartRefresh)
    trials.addData('baselineImage.stopped', baselineImage.tStopRefresh)
    imageId=imageId+1
    
    # ------Prepare to start Routine "imageShow"-------
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    image.setImage(Original)
    
    start_time = time.time()
    allGazeData = []
    # keep track of which components have finished
    imageShowComponents = [image]
    for thisComponent in imageShowComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imageShowClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "imageShow"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = imageShowClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imageShowClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        print(global_gaze_data)
        time.sleep(1/frequency)
        print(getTimeStamp())
        
        allGazeData.append(global_gaze_data)
        ###################collecting data for csv final reading(main image)
        csvGaze.append(['Trial'+str(counter),'stimuli',global_gaze_data['device_time_stamp'],global_gaze_data['left_pupil_diameter'],global_gaze_data['left_pupil_validity'],global_gaze_data['right_pupil_diameter'],global_gaze_data['right_pupil_validity']])
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imageShowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "imageShow"-------
    for thisComponent in imageShowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    imageId=imageId+1
    
    # ------Prepare to start Routine "Feedback"-------
    # update component parameters for each repeat
    rating.reset()
    NextImagePress.keys = []
    NextImagePress.rt = []
    RatingText.setText('Do you like this image?')
    # keep track of which components have finished
    FeedbackComponents = [rating, NextImagePress, RatingText]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # *NextImagePress* updates
        waitOnFlip = False
        if NextImagePress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextImagePress.frameNStart = frameN  # exact frame index
            NextImagePress.tStart = t  # local t and not account for scr refresh
            NextImagePress.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextImagePress, 'tStartRefresh')  # time at next scr refresh
            NextImagePress.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(NextImagePress.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextImagePress.status == STARTED and not waitOnFlip:
            theseKeys = NextImagePress.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *RatingText* updates
        if RatingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RatingText.frameNStart = frameN  # exact frame index
            RatingText.tStart = t  # local t and not account for scr refresh
            RatingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingText, 'tStartRefresh')  # time at next scr refresh
            RatingText.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    trials.addData('rating.started', rating.tStart)
    trials.addData('rating.stopped', rating.tStop)
    trials.addData('RatingText.started', RatingText.tStartRefresh)
    trials.addData('RatingText.stopped', RatingText.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

    ######### adding feedback to all the readings with this subroutine
    for i in csvGaze:
        i.append(rating.getRating())
    ### writing finally to a csv
    writer.writerows(csvGaze)
    counter += 1
    #################################
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Thanks"-------
# update component parameters for each repeat
StopTrialPress.keys = []
StopTrialPress.rt = []
# keep track of which components have finished
ThanksComponents = [ThanksText, StopTrialPress]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Thanks"-------
while continueRoutine:
    # get current time
    t = ThanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThanksText* updates
    if ThanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ThanksText.frameNStart = frameN  # exact frame index
        ThanksText.tStart = t  # local t and not account for scr refresh
        ThanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThanksText, 'tStartRefresh')  # time at next scr refresh
        ThanksText.setAutoDraw(True)
    
    # *StopTrialPress* updates
    waitOnFlip = False
    if StopTrialPress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        StopTrialPress.frameNStart = frameN  # exact frame index
        StopTrialPress.tStart = t  # local t and not account for scr refresh
        StopTrialPress.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(StopTrialPress, 'tStartRefresh')  # time at next scr refresh
        StopTrialPress.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(StopTrialPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if StopTrialPress.status == STARTED and not waitOnFlip:
        theseKeys = StopTrialPress.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ThanksText.started', ThanksText.tStartRefresh)
thisExp.addData('ThanksText.stopped', ThanksText.tStopRefresh)
# the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
csvfile.close()# close the csv for experiment
core.quit()
