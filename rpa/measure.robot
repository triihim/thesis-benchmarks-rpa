*** Settings ***
Library    SeleniumLibrary
Library    Process
Library    OperatingSystem

Suite Setup       Setup RPA
Suite Teardown    Teardown RPA

*** Variables ***
${browser}    chrome
${url}    http://localhost:3000/ 
${framework}    na
${iteration}    1
${rendercount}     25000

*** Keywords ***
Setup RPA
    Open Browser     ${url}    ${browser}
    Wait Until Page Contains    Ready to start
    Input Text    tag:input    ${rendercount}
    Click Button    id=btnGenerate
    Wait Until Page Contains    Ready to render

Teardown RPA
    Close Browser
    Start Process    python    ./scripts/profile.py    ${browser}     ${framework}     ${iteration}
    Start Process    python    ./scripts/aggregate.py    ${browser}     ${framework}     ${iteration}

Begin Measurement
    Sleep    1s
    Start Process    IntelPowerGadget.exe     -start
    Sleep    1s

End Measruement
    Sleep    1s
    Start Process    IntelPowerGadget.exe     -stop
    Sleep    1s


Rename Measurement File
    [Arguments]    ${name}
    Move File    ./measurements/measurement*    ./csv/${browser}_${framework}_${name}_${iteration}.csv 

*** Tasks ***
Measure Render
    Begin Measurement
    Click Button    id=btnRender
    Wait Until Page Contains    Ready to update
    End Measruement
    Rename Measurement File    render

Measure Update
    Begin Measurement
    Click Button    id=btnUpdate
    Wait Until Page Contains    Ready to remove
    End Measruement
    Rename Measurement File    update

Measure Remove
    Begin Measurement
    Click Button    id=btnRemove
    Wait Until Page Contains    Finished
    End Measruement
    Rename Measurement File    remove
