Version 0.1 - VERY draft of rhaptos.swordclient.blogpub

This Pyramid app started as the one direct result of the first PloneSA sprint held at the Open Innovation Studio in Cape Town on the 29th of June 2011. The sprint outline and briefing can be found at: https://docs.google.com/document/d/1bQWd2XZKCGycHrd-zbdEV5f62U8UP645GahYeXuDhMI/edit?authkey=CJWjxs0I&hl=en_US

The goal is to create an open web service that can read a blog post, convert it to a SWORD package and upload it to a compliant repository. As per the google document above.

Task 2: (SWORD Client) Web service to publish a blog entry to a SWORD repository
Develop a web service that allows you to publish a blog entry and all the media it references to a SWORD v2 repository.

    The service should use the RSS feed of the blog to extract all the necessary metadata.
    The user should be allowed to verify extracted metadata and add any missing metadata on simple form.
    The user must select the licencing that applies to the package.
    The user should be allowed to specify a Google Analytics tracking code. The service should remember the tracking code entered using a cookie so that the user doesn't have to retype it each time. (We will need to come up with a metadata field (and namespace) to hold this).
    It should be possible to embed this service into an existing site - similar to what Facebook and Twitter does.
    May eventually want to be able to choose blog entries via a category/tag.

This ulterior goal of this task is to create a service that publishes educational blog entries as Connexions remixable modules.

TODO:
- recursively read the blog post and collect all relevant resources.
- display and update the metadata.
- display the list of possible collections to add this package to.
- create the SWORD package (reuse as much as possible from https://github.com/jbeyers/rhaptos.swordclient.cli)
- PUT the package into the selected collection in the selected repository.
- Lots of styling.
