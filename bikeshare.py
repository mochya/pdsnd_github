import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city=''
    month=''
    day=''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in ['chicago', 'new york city', 'washington']:
        city=input('Please specify a city name from chicago, new york city, and washington:').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month=input('Please specify a month from january, february, march, april, may, june, and all:').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in ['monday', 'tuesday', 'wednsday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day=input('Please specify a month from monday, tuesday, wednsday, thursday, friday, saturday, sunday, and all:').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['stdtc'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['stdtc'].dt.month
    df['day_of_week'] = df['stdtc'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
 
# filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...\n')

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is {}".format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is {}".format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['stdtc'].dt.hour.mode()[0]
    print("The most common start hour is {}".format(common_hour))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}".format(common_sstation))

    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print("The most commonly used end station is {}".format(common_estation))

    # TO DO: display most frequent combination of start station and end station trip
    df['se_combine'] = df['Start Station'] + df['End Station']
    common_combine = df['se_combine'].mode()[0]
    print("The most common frequent combination of start station and end station trip is {}".format(common_combine))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...\n')

    # TO DO: display total travel time
    total_second = df['Trip Duration'].sum()
    print("The total travel time is {} in seconds.".format(total_second))

    # TO DO: display mean travel time
    mean_second = df['Trip Duration'].mean()
    print("The average travel time is {}.".format(mean_second))
    
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The cuonts of user types are:")
    print(user_types)

    # TO DO: Display counts of gender
    if city in ['chicago', 'new york city']:
        gender = df['Gender'].value_counts()
        print("The cuonts of gender are:")
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        birth_min = df['Birth Year'].min()
        print("The earliest year of birth is: {}".format(birth_min))
        birth_max = df['Birth Year'].max()
        print("The most recent year of birth is: {}".format(birth_max))
        birth_mode = df['Birth Year'].mode()[0]
        print("The most common year of birth is: {}".format(birth_mode))

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print("The statistics would be display upon bikeshare data for {} in {} on {}.".format(city, month, day))
        
        start=0
        while True:
            first5row = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
            if first5row.lower() != 'yes':
                break
            else:
                print("Displaying data from line {} to {}.".format(start, start+4))
                print(df[start: start+5])
                start += 5
                
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
