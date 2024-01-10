from django.test import TestCase

# Create your tests here.


# {% if p.images.all %}
                                
#                                 {% for image in p.images.all %}
#                                     <div style="position: relative; display: inline-block;">
#                                         <img style="height: 200px; width: auto; display: block;" src="{{ image.image.url }}" alt="Post Image">
#                                         <a title="Download" style="position: absolute; top: 0; right: 0; margin: 5px 5px;"
#                                         href="{% url 'download_image' image.id %}" download>
#                                             <i class="fa-solid fa-download fa-lg"></i>
#                                         </a>
#                                     </div>
#                                 {% endfor %}
                                    
#                                 {% endif %}

# image = get_object_or_404(Image, id=image_id)
#     file_path = image.image.path

#     # Create response and set headers for downloading a single image
#     with open(file_path, 'rb') as file:
#         response = HttpResponse(file.read(), content_type='application/octet-stream')
#         response['Content-Disposition'] = f'attachment; filename={image.image.name}'
#         return response


# author = User.objects.get(username = user)
#         authorprofile = Profile.objects.get(user = user)
#         text = request.POST['text']
#         postimgs = request.FILES.getlist('image', None)
#         print(postimgs)
#         post = Post.objects.create(author = author, authorprofile = authorprofile, username = user, text=text)
        
#         if post:
#             for postimg in postimgs:
#                 Image.objects.create(post = post, image = postimg)
#             profile.total_post = profile.total_post + 1
#             profile.save()
    