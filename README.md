# GrowthForge

GrowthForge is a simplified feedback exchange platform designed to facilitate
periodic feedback between individuals within specific projects. It aims to
streamline communication and insights sharing, enhancing project collaboration
and personal development.

- Documentation: <https://opensciencelabs.github.io/growth-forge>

## Features

GrowthForge includes several key features to manage feedback efficiently:

### Projects

- **Creation and Management**: Admin users can create and manage projects, each
  with specific goals and participants.
- **Global Access Control**: For each project, certain individuals can be
  designated to have global access to all feedback related to that project,
  ensuring oversight and support where needed.

### People

- **Profile Management**: Admin users can create profiles for individuals who
  will be associated with zero or more projects. The email used will serve as a
  constraint for login; only individuals registered by an admin can log into the
  platform. New users will receive a random password via email.
- **Project Association**: From the people form, users can select projects to
  associate with an individual, allowing for flexible project participation.
- **Login**: Only individuals registered by an admin can log into the platform.

### Links

- **Feedback Pairing**: The platform allows the creation of links between two
  individuals, enabling them to exchange feedback periodically. Only an admin
  can create this link. The admin must define the periodicity (daily, weekly,
  monthly) and a number that specifies "Every X times" it will be repeated.
- **Supervisor Assignment**: Each link can have designated supervisors who are
  granted access to read all the feedback exchanged within that link, ensuring
  appropriate oversight and support.

### Feedback

- **Periodic Exchange**: Feedback is exchanged periodically (e.g., weekly)
  between linked individuals, fostering continuous growth and development.
- **Visibility and Access**: Feedback visibility is controlled through project
  associations, link-specific supervisors, and global access roles, ensuring
  information is shared with the right people.

## Usage

- **Managing Projects**: Navigate to the Projects section to create, view, and
  edit projects.
- **Adding People**: In the People form, you can add individuals to the system
  and associate them with projects.
- **Creating Links**: Use the Link form to connect two people for feedback
  exchange and assign supervisors to oversee the feedback.
- **Exchanging Feedback**: Linked individuals can start exchanging feedback as
  per the defined periodic schedule.

## Contributing

GrowthForge is open for contributions. Whether it's feature requests, bug
reports, or code contributions, we welcome your input to make GrowthForge
better. Please see our contributing guidelines for more information.

## License

GrowthForge is licensed under the BSD 3-Clause License.

## Contact

For support or to get in touch with the developers, please open an issue.

---

We hope GrowthForge enhances your project collaboration and personal development
efforts!
