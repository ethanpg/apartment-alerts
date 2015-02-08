# Hack Housing: Apartment Alerts

This project implements an SMS alert system for low-income property managers to alert prospective tenants that an apartment matching their criteria has become available.

This application was developed on February 6-8th, 2015 for the Zillow's Hack Housing event.

To sign up to receive alerts for our sample building, send a text message to (301)761-5786 with the following form:

   signup <name>, <#> bedrooms, $<income>.

For instance, a propspective tenant named Sarah, who makes $18,000 a year and is looking for a 1 bedroom apartment can send:

  signup Sarah, 1 bdrm, $18000.

When the building manager has an apartment available, they can text all waiting applicants at once by sending the message:

   alert <#> bedroom, <income minimum>-<income maximum>. <any additional message>

For example, if a 1 bedroom becomes available to those making between $10,000 and $20,000, the building manager would send the text:

   alert 1 bedroom, 10,000-20,000. Opening 3/1

Sarah, and anyone else signed up would receive the message:

    Unit opening at 1234 Some St: Opening 3/1. Call 206-867-5309.

The building address and contact phone number are populated automatically from the database.

Note that for ease of demonstration, anyone is currently allowed to send alerts. In the production system, alert functionality would be limited to the manager.


## Challenge and Approach

Our challenge was to make build a system that could make real improvements in the efficiency of finding affordable housing. Key to our approach is the belief that low-income renters are not suffering from a shortage of information. Residents are already aware of the low-income housing in their neighborhoods.

From our team's real-world experience at a non-profit housing developer, we have identified an actual problem faced by property managers and applicants: there is usually no automated wait-list for housing. This leads to applicants having to call daily to dozens of buildings in their neighborhoods. Property managers are burdened fielding repeat phone calls.

Additionally, non-profits have very little ability to adopt new IT systems. Instead of a central inventory management system, which would face huge hurtles to adoption, we require no integration whatsoever with existing IT systems, and put adoption in the hands of the individual building managers--the ones that stand to gain the most by adopting our system.


## Team Members

Our team is comprised of:

- [@ethanpg](http://twitter.com/ethanpg) - Founder of civic tech startup Seattle in Progress.
- [@whitnuld](http://twitter.com/whitnuld) - Whitney Rearick, Low Income Housing Institute.
- Jeffrey Wall, Engineering Manager at Microsoft.

## Technologies, APIs, and Datasets Utilized

We made use of:

- Python + Django stack.
- Twilio for SMS integration.

## Contributing

Our code is licensed under the [MIT License](LICENSE.md). Pull requests will be accepted to this repo, pending review and approval.
