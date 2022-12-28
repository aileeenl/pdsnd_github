import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_input(input_data,input_cat):
    """
    When checking user input:
    input_data - is the input from user
    input_cat - is the input category: 1 = city, 2 = month, 3 = day

    """
    while True:
        input_read = input(input_data).lower()

        if input_read in ['chicago', 'new york city', 'washington', 'yes', 'no'] and input_cat == 1:
                break
        elif input_read in ['january', 'february', 'march', 'april', 'may', 'june', 'yes', 'no'] and input_cat == 2:
                break
        elif input_read in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'yes', 'no'] and input_cat == 3:
                break
        else:
                if input_cat == 1 or input_cat == 2 or input_cat == 3:
                    print("\nOops! What you just entered was incorrect")

    return input_read


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_input("\nPlease enter either chicago, new york city or washington to explore that city\'s bikeshare data.\n",1)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = check_input("\nPlease enter a month from january to june to explore that month\'s bikeshare data.\n",2)

         # use the index of the month list to get the corresponding int
    month = month.index(month) + 1

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_input("\nPlease enter any day of the week from sunday to saturday to explore that day\'s bikeshare data.\n",3)


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    month == ['janaury', 'february', 'march', 'april', 'may', 'june', 'all']

    # filter by month to create the new dataframe
    df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    day = day.index(day) + 1

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is:', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station :', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station :', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    most_popular_start_and_end_stations = group_field.size().sort_values(ascending=False).head(1)
    print('The most popular combination of start and end stations are:\n', most_popular_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time :', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time :', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCount of user types:\n')
    print(df['User Type'].value_counts())
    print('-'*40)

def gender_stats(gender):

    try:
        city = ('chicago', 'new york city', 'washington')

    # TO DO: Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        print('-'*40)        

    # Skip gender/birth year stats for Washington due to no stats available
    except KeyError:
        print('\nThere are no stats available for this city\n')



def birth_year_stats(df):
    # TO DO: Display earliest, most recent, and most common year of birth
    print('Birth Year Stats:')
    most_common_year = df['Birth Year'].mode()[0]
    print('Most Common Year:',most_common_year)
    most_recent_year = df['Birth Year'].max()
    print('Most Recent Year:',most_recent_year)
    earliest_year = df['Birth Year'].min()
    print('Earliest Year:',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, data):
    """
    shows lines of raw data upon request

    """
    city_data = pd.read_csv[("chicago.csv"), ("new york city. csv"), ("washington.csv")]

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(data.iloc[0:5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	    main()
