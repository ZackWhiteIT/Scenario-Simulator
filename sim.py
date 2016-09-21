import json
import textwrap
import random


def generate_response(options_dict):
    """ Return a response ID for the bot """
    return random.randint(1, len(options_dict)) - 1


def calculate_results(results_dict, user_response, bot_response):
    """ Lookup the proper result from the JSON results matrix for a given scenario """
    result_data = ''
    for result in results_dict:
        if int(result['user_selection']) == int(user_response) and int(result['bot_selection']) == int(bot_response):
            result_data = result['result']
    return result_data


def display_scenario(scenario_dict):
    """ Present user with a scenario and prompt them for a response """
    wrapper = textwrap.TextWrapper(
        width=70, break_long_words=False, replace_whitespace=False)
    print('\n')
    print(scenario_dict['name'].upper())
    print('-' * 70 + '\n')
    print(wrapper.fill(scenario_dict['story']))
    question = '\nWhat do you do?\n'
    for option in scenario_dict['options']:
        question += "\n{}) {}".format(option['id'], option['text'])
    question += '\n\nOption Number: '
    user_response = int(get_user_response(question))
    return user_response


def load_scenario(json_file_path):
    """ Load scenario from JSON """
    json_file = open(json_file_path, 'r')
    parsed_json = json.loads(json_file.read())
    json_file.close()
    return parsed_json


def get_user_response(question):
    """ Get user input """
    # TODO: Add more input filtering (require int in range of options)
    return raw_input(question)


def main(args=None):
    """ Loops over scenarios """
    scenarios_json = load_scenario('scenarios.json')
    for scenario in scenarios_json['scenarios']:
        user_response = display_scenario(scenario)
        bot_response = generate_response(scenario['bot_options'])
        print(scenario['bot_options'][bot_response]['text'])
        result = calculate_results(
            scenario['results_array'], user_response, bot_response + 1)
        print("\n{}".format(result))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
