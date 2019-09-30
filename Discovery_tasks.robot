*** Settings ***
Documentation     Suite description
Library           keywords

*** Variables ***
${show_keyword}     apollo
*** Test Cases ***
Task1
    Go To Discovery Home Page
    Go To Footer
    Click See All Shows
    Search Show   ${show_keyword}
    Add To Favourite
    Go To My Videos


Task2
    Go To Discovery Home Page
    Move To Popular Shows Dot Pager
    Go To Last Popular Show
    Explore The Show
    Show More Episode
    ${map}=    Get All Episodes Title And Time
    ${title_duration_map}=    create dictionary    ${map}
    Export Title Duration To file    ${title_duration_map}
