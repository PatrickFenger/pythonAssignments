def crime_location(url, amount_value=2):
    xl_sheet1 = get_sheet(url)
    state = ""
    dict = {}
    dict_plot = {}
    temp_dict = {}
    amount_sum = 0
    for row_idx in range(4, 9297):
        temp_state = list(str(xl_sheet1.cell(row_idx, 0)).split(":"))[1]
        city = list(str(xl_sheet1.cell(row_idx, 1)).split(":"))[1]
        temp_list = []
        # temp_dict[city]=[]
        temp_sum = 0.0

        if re.match("\'([A-Za-z]+)\'", temp_state):
            temp_dict = {}
            violent_crime_sum = 0.0
            murder_sum = 0.0
            rape1_sum = 0.0
            rape_legacy_sum = 0.0
            robber_sum = 0.0
            assault_sum = 0.0
            property_sum = 0.0
            burglary_sum = 0.0
            larency_sum = 0.0
            m_vechiel_sum = 0.0
            arson_sum = 0.0
            state = temp_state

            if amount_sum == amount_value:
                print("in")
                print(dict)
                return dict
            amount_sum += 1
            dict[state] = {}
        for col in range(3, 14):
            temp_value = list(str(xl_sheet1.cell(row_idx, col)).split(":"))[1]
            if col == 3:

                try:
                    violent_crime_sum += float(temp_value)
                    temp_dict["violent_crime_sum"] = violent_crime_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 4:
                try:
                    murder_sum += float(temp_value)
                    temp_dict["murder_sum"] = murder_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 5:
                try:
                    rape1_sum += float(temp_value)
                    temp_dict["rape1"] = rape1_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 6:
                try:
                    rape_legacy_sum += float(temp_value)
                    temp_dict["rape_legacy"] = rape_legacy_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 7:
                try:
                    robber_sum += float(temp_value)
                    temp_dict["robbery"] = robber_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 8:
                try:
                    assault_sum += float(temp_value)
                    temp_dict["assault"] = assault_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 9:
                try:
                    property_sum += float(temp_value)
                    temp_dict["property"] = property_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 10:
                try:
                    burglary_sum += float(temp_value)
                    temp_dict["burglary"] = burglary_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 11:
                try:
                    larency_sum += float(temp_value)
                    temp_dict["larency"] = larency_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 12:
                try:
                    m_vechiel_sum += float(temp_value)
                    temp_dict["motor veachiel"] = m_vechiel_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
            elif col == 13:
                try:
                    arson_sum += float(temp_value)
                    temp_dict["arson"] = arson_sum
                    dict[state] = temp_dict
                    # temp_sum += float(temp_value)
                except ValueError:
                    print("not number")
    # return dict
    # dict_plot[state].
    ##temp_dict[city].append(temp_sum)

    # print(dict_plot)
# change_in_crime(url)
# print("svar spørgs 2",most_common_type_of_crime())