# app/utils.py

import calendar

def parse_data_to_stats(json):
    if len(json["response"]) == 1:
        response = json["response"][0]
        cases = response["cases"]
        deaths = response["deaths"]

        [date, time] = response["time"].split('T')

        title = _parse_title(date, time)
        stats = _parse_stats(cases, deaths)

        return "% s\n\n% s"% (title, stats)

    return "No data found. Please try again later."  


def parse_sby_data_to_stats(json):
    if json:
        msg_title = "\U0001F4CD *SURABAYA*"
        stats = []
        for title in json.keys():
            data = json[title]

            if data["change"] == 0:
                stats.append("% s: % s (No change)"% (
                    title,
                    data["last_value"]
                ))
            else:    
                stats.append("% s: % s (% s % s%%, % s)"% (
                    title,
                    data["last_value"],
                    "\U0001F4C9" if data["change"] < 0 else "\U0001F4C8",
                    str(round(abs(data["change"]) * 100, 2)),
                    data["previous_value"]
                ))

        return "% s\n\n% s"% (msg_title, "\n".join(stats))

    return "No data found for Surabaya. Please try again later."

def _parse_title(date, time):
    [y, m, d] = date.split('-')
    formatted_date = "% s % s % s"% (d, calendar.month_name[int(m)], y)

    return "*Indonesia Covid-19 Status Update for % s*\n_Data Last Updated: % s_"% \
        (formatted_date, time)    


def _parse_stats(cases, deaths):
    new_cases = (cases["new"] or "-").replace('+', '')
    new_deaths = (deaths["new"] or "-").replace('+', '')

    new = "*New*\nCases: % s\nDeaths: % s"% (new_cases, new_deaths)

    recovered = cases["recovered"]
    critical = cases["critical"]
    total_deaths = deaths["total"]
    total_cases = cases["total"]
    active_cases = cases["active"]

    total = "*Total*\nRecovered: % s\nCritical: % s\nDeaths: % s\nCases: % s (Active: % s)"% \
        (recovered, critical, total_deaths, total_cases, active_cases)

    return "% s\n\n% s"% (new, total)    

