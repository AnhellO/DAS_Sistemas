                             Resume of Best Practices for compose-managed Python

In general, our containerized development cycle consists of writing/updating code, building, running and debugging it.

For the building and running phase, as most of the time we actually have to wait, we want these phases to go pretty quick such that we focus on coding and debugging.

We now analyze how to optimize the build phase during development. The build phase corresponds to image build time when we change the Python source code. The image needs to be rebuilt in order to get the Python code updates in the container before launching it.

We can however apply code changes without having to build the image. We can do this simply by bind-mounting the local source directory to its path in the container. For this, we update the compose file as follows.

Furthermore, we can avoid re-starting the container if we run inside it a reloader process that watches for file changes and triggers the restart of the Python process once a change is detected. We need to make sure we have bind-mounted the source code in the Compose file