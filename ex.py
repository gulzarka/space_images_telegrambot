def get_launch_id_list():
    response = requests.get("https://api.spacexdata.com/v5/launches")
    response.raise_for_status()
    response_content = response.json()
    launch_id_list = []
    formatted_id_list = str(launch_id_list)
    for content in response_content:
        if not content['links']['flickr']['original'] == []:
            launch_id = content['id']
            launch_id_list.append(launch_id)
            return launch_id_list 