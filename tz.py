import datetime
import pytz
import tzlocal

# zona de fus orar pentru ora introdusa
user_time_zone = pytz.timezone(tzlocal.get_localzone_name())

# szona de fus orar pentru New York
newyork_tz = pytz.timezone('US/Eastern')

while True:
    try:
        # obtine ora introdusa de utilizator
        user_time_str = input("Introdu ora dorita (HH:MM): ")

        # obtine anul, luna, si ziua curenta
        current_date = datetime.datetime.now()

        # anul, luna, si ziua curenta la ora introdusa de utilizator
        user_time = datetime.datetime.strptime(user_time_str, "%H:%M")
        user_time = user_time.replace(
            year=current_date.year, month=current_date.month, day=current_date.day)

        # ora introdusa la ora UTC
        user_time = user_time_zone.localize(user_time)

        # ora introdusa la ora New York
        ny_time = user_time.astimezone(newyork_tz)

        # afiseaza ora New York
        print("Ora convertita in fusul orar New York este " +
              ny_time.strftime("%H:%M"))
        break

    except ValueError:
        print("Ora a fost introdusa gresit. Introdu ora in formatul HH:MM")