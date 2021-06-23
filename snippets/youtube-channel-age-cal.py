import datetime
from datetime import date
#youtube_date_stirng = "jun 13, 2020"
#just a use hashmap for months and data associated with it.
months_dict = {
  "Jan": {
    "name": "January",
    "short": "Jan",
    "number": 1,
    "days": 31
  },
  "Feb": {
    "name": "February",
    "short": "Feb",
    "number": 2,
    "days": 28
  },
  "Mar": {
    "name": "March",
    "short": "Mar",
    "number": 3,
    "days": 31
  },
  "Apr": {
    "name": "April",
    "short": "Apr",
    "number": 4,
    "days": 30
  },
  "May": {
    "name": "May",
    "short": "May",
    "number": 5,
    "days": 31
  },
  "Jun": {
    "name": "June",
    "short": "Jun",
    "number": 6,
    "days": 30
  },
  "Jul": {
    "name": "July",
    "short": "Jul",
    "number": 7,
    "days": 31
  },
  "Aug": {
    "name": "August",
    "short": "Aug",
    "number": 8,
    "days": 31
  },
  "Sep": {
    "name": "September",
    "short": "Sep",
    "number": 9,
    "days": 30
  },
  "Oct": {
    "name": "October",
    "short": "Oct",
    "number": 10,
    "days": 31
  },
  "Nov": {
    "name": "November",
    "short": "Nov",
    "number": 11,
    "days": 30
  },
  "Dec": {
    "name": "December",
    "short": "Dec",
    "number": 12,
    "days": 31
  }
}
   
#returns parsed a tuple in format (yy,mm,dd) : input should be in string datatype with 
def getYoutubeJoinedDateStringToyymmddFormat(youtube_date_stirng):
    youtube_date_stirng = youtube_date_stirng.replace(",","").split(" ")
    dd = int(youtube_date_stirng[1])
    mm = youtube_date_stirng[0].title()
    yy = int(youtube_date_stirng[2])
    mm = int(months_dict[mm]["number"])
    return yy, mm, dd

#returns current date in tuple ex. (yy,mm,dd) | no input required.
def currentDateddmmyy():
    dataobj = datetime.datetime.now()
    dd = dataobj.day
    mm = dataobj.month
    yy = dataobj.year
    return yy, mm, dd
#This function will calculate the difference between current date and joined date in days format (ex. 337) which is an integer datatype
def getTheAgeOfThisChannelInDaysFormat(joined_date):
    current_obj_tuple = currentDateddmmyy()
    current_date = date(current_obj_tuple[0],current_obj_tuple[1],current_obj_tuple[2])
    joined_obj_tuple = getYoutubeJoinedDateStringToyymmddFormat("jun 13, 2020")
    joined_date = date(joined_obj_tuple[0],joined_obj_tuple[1],joined_obj_tuple[2])
    delta = current_date - joined_date
    
    return delta.days

#This function will calculate the difference between current date and joined date in years format (ex. 337) which is an integer datatype
def getTheAgeOfThisChannelInYearsFormat(joined_date):
    current_obj_tuple = currentDateddmmyy()
    current_date = date(current_obj_tuple[0],current_obj_tuple[1],current_obj_tuple[2])
    joined_obj_tuple = getYoutubeJoinedDateStringToyymmddFormat("jun 13, 2020")
    joined_date = date(joined_obj_tuple[0],joined_obj_tuple[1],joined_obj_tuple[2])
    delta = current_date - joined_date
    years = round(delta.days/365)
    return years

