# Alarm Clock GUI 

## A simple alarm clock app, made by using PyQt5.

<img width="500" alt="Screen Shot 2021-01-29 at 10 37 05 PM" src="https://user-images.githubusercontent.com/62267311/106346249-9c73ba80-6283-11eb-9c8d-bfb1ffcae408.png">

Once the user runs the program, they will see a clean, simple main menu, which also displays the current date and time. This clock has 4 functions: Create Alarm, Remove Alarm, View Alarms, and Quit.

### Create Alarm:

<img width="500" alt="Screen Shot 2021-01-29 at 10 37 36 PM" src="https://user-images.githubusercontent.com/62267311/106346285-faa09d80-6283-11eb-9c56-485ab3621630.png">

Consists of 2 Spinboxes, whose values can be by using the up/down buttons, or by typing in desired time. Clicking the "OK" button will save the desired time and will alert the user that it has done so by updating the "Note" text to say "Alarm Saved!"
The new alarm will be saved into the app.


### Remove Alarm:

<img width="500" alt="Screen Shot 2021-01-29 at 10 37 51 PM" src="https://user-images.githubusercontent.com/62267311/106346357-8e726980-6284-11eb-83f0-ea69a51ba61a.png">

Clicking the "Remove Alarm" button will cause a List Widget to appear. The List Widget will hold the alarms that the user has made. If no alarms were made, a Message Box will appear, alerting the user that there are no alarms to remove.

If the user did make an alarm, and would like to delete it, they would click on the alarm they'd like to delete and click the "OK" button. 
The window would need to be reopened to reflect the new changes.


### View Alarm:

<img width="500" alt="Screen Shot 2021-01-29 at 10 38 55 PM" src="https://user-images.githubusercontent.com/62267311/106346465-6df6df00-6285-11eb-9cb7-def67a5bd8cf.png">

This choice will display any alarms that the user has made. If there are no alarms, a Message Box will alert the user that there are no alarms to view.

## Quit:

Clicking this will terminate the application.
