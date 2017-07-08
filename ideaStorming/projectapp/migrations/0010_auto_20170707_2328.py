# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 03:28
from __future__ import unicode_literals

from django.db import migrations

import random


def load_projects(apps, schema_editor):
	Project = apps.get_model("projectapp", "Project")
	User = apps.get_model("authapp", "User")

	tag_list = [i for i in range(1, 51)]

	users = User.objects.all()
	app_project = Project(
		title = " Duis semper eget", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[1],
		mark = 2.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "elit quis blandit", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[1],
		mark = 1.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "Ut ac massa vitae velit", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[1],
		mark = 1.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "tincidunt ut id magna", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[2],
		mark = 0.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "at dignissim. Cras", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 4.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "iaculis nibh id dolor aliquam", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 0.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "Sed luctus a augue at finibus", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 2.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "Phasellus bibendum", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 3.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "ante vitae cursus elementum", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 1.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "Fusce sem purus, feugiat", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 0.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "elementum porta velit", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[1],
		mark = 3.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "Nunc ac sollicitudin nisi", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[1],
		mark = 1.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "Donec efficitur risus sit amet", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[1],
		mark = 4.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "rutrum fringilla", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[0],
		mark = 3.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "Sed et enim facilisis urna", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[1],
		mark = 1.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "sagittis consequat sit", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 3.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = " Ut ac neque sollicitudin", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 0.0
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)	
	app_project = Project(
		title = "malesuada justo sit amet", 
		summary = "Morbi vitae dui purus. Duis nisl ante, varius quis varius sed, fermentum sit amet quam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget ornare sapien. Maecenas vestibulum lorem vel sem ornare porta. Nunc efficitur sem in quam lobortis iaculis.",
		advantages = "Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed eu ullamcorper dolor, nec commodo elit. Praesent eget sagittis est. Praesent eget cursus purus.",
		investment = "$100 - $300 USD",
		user  = users[3],
		mark = 2.5
	)
	app_project.save()
	for tag in random.sample(tag_list,  random.randint(1, 7)):
		app_project.tags.add(tag)

class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0009_auto_20170706_2237'),
    ]

    operations = [
    	migrations.RunPython(load_projects),
    ]
