import  facebook as fb

api =  'api token from meta (access_token )'
graph = fb.GRAPHAPI(access_token=api)

# post upload
graph.put_object(parent_object='me',connection_name='feed',message='Hi! How are you',link='https://www.google.com')
print('Post Done')

# Upload an image with a caption.
graph.put_photo(image=open('img.jpg', 'rb'),message='Look at this cool photo!')

# Get the message from a post.
post = graph.get_object(id='post_id', fields='message')
print(post['message'])

# Write a comment on a post.
graph.put_object(parent_object='post_id', connection_name='comments',message='First!')

# Get the comments from a post.
comments = graph.get_connections(id='post_id', connection_name='comments')

# Pull Comment ==> Writes the given message as a comment on an object.
graph.put_comment(object_id='post_id', message='Great post...')

# Get the active user's friends.
friends = graph.get_connections(id='me', connection_name='friends')

# put_like == > Writes a like to the given object.
graph.put_like(object_id='comment_id')

# Upload a photo to an album.
graph.put_photo(image=open("img.jpg", 'rb'),album_path=album_id + "/photos")

# Upload a profile photo for a Page.
graph.put_photo(image=open("img.jpg", 'rb'),album_path=page_id + "/picture")

# Delete Photo
graph.delete_object(id='post_id')

# Retrieve the number of people who say that they are attending or declining  to attend a specific event.
event = graph.get_object(id='event_id',fields='attending_count,declined_count')
print(event['attending_count'])
print(event['declined_count'])

# Get the time two different posts were created.
post_ids = ['post_id_1', 'post_id_2']
posts = graph.get_objects(ids=post_ids, fields="created_time")
for post in posts:
    print(post['created_time'])