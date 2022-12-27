ControlFocus("Open","", "Edit1")
$Date = @MDAY & '_' & @MON & '_' & @YEAR
ControlSetText("Open", "", "Edit1", "C:\Users\User\PyProjects\newsViewer\tempIMG\" & $Date & ".jpg")
ControlClick("Open", "", "Button1")