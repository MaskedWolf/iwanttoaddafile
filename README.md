## Inspiration
- MKN official SOP list is cluttered & not user-friendly
- Confusion as SOPs change frequently & are region-based
- People seeking employment and advertisement (especially small businesses)
- Many services & volunteer projects without an - aggregator to display them all
- Many who want to attempt their own start-ups/projects lack a platform to promote locally

## What it does
- User selects their state & vaccination status
- SOP information is customised according to above information
- Aggregator to improve business activity by promoting services 
- Unifies different types of services/phase SOPs in one web app for easy information access
- Random generator to suggest fun and useful learning content

#### Pages:
- Home feed: displays list of businesses & other activities currently accessible to the user, which can be filtered via tags
- SOPs: simplified list of current SOPs specific to the user, listing what types of activities are allowed & not allowed, based on their state and vaccination status
- Submit: form for business owners etc. to submit information for their endeavours with location/contact information & tags. Submissions will be displayed publicly on the feed once uploaded.
- About/Contact: links to the team’s social pages, as well as links to the official MKN website & hotline numbers
- Random generator: suggest external learning content to fend off boredoom

## How we built it
- Brainstormed problems & narrowed down to those we could tackle
- Planned a sitemap listing all required features

#### Frontend
- Began by brainstorming a UI which is simple to understand at a glance (user-friendly), in contrast to a cluttered display
- Layout aimed at less tech-savvy members, given a more visual presentation like pictograms to accomodate language barrier
- Simple infographics for SOP page acting like a summary
- Designed scrolling feed that users would be familiar with by emulating popular social media
- On all pages, we fixed a header as a dropdown selector, & a footer as navigation menu

#### Backend
- Use Python Django as Backend
- Create a Django App for each uses: SOP details, Business activities as blog feed, Login user system, Random generator for learning resources
- Apply Model-View-Template pattern


## Challenges we ran into
#### Challenge 1: Coding collaboratively as a team
- Hosting a website on our own individual computers is not efficient for collaboration & communication

#### Solution 1: Coding collaboratively as a team
- Use repl.it IDE to code collaboratively and to host the website

#### Challenge 2: Technical issues
- Branch issue: The github extension on replit does not support coding on different branches simultaneously. Changing a branch will cause all collaborators to be transferred to that branch, losing all changes that have not been pushed or committed.
- Problem with pull & merge on Github. Doesn’t sync with replit
- Network issues, some loss of progress as different team members update the project out of sync

#### Solution 2: Technical issues
- Minimise the number of members working on the same page concurrently by dividing tasks & periodically checking back on each other

#### Challenge 3: Execution & Feasibility
- Manpower issue with updating SOPs in real-time

#### Solution 3: Execution & Feasibility
- Possible partnership with government bodies to provide
- Possible automation with web-scraping.
- Each solution also brings up other factors to be considered:
  - Must consider what returns MKN or other government bodies will gain from the project
text-recognition software may not be reliable, so still requires manpower to check for accuracy

#### Challenge 4: Unique selling property
- Our website has to provide unique value that helps users the most

#### Solution 4: Unique selling property
- Combination of social media and informative web app UI 
- Understandable UI design (e.g. Icons representing SOPs instead of lengthy text)


## Accomplishments that we're proud of
- Previously, most of us had no experience in web development. We have learnt a ton about frontend development and Python Django.

## What we learned
- An appreciation for how difficult it is to create a social media site & info aggregator
- An appreciation for the manpower required
- We cannot cater to every demographic & solve every issue, so it is better to specify a target & deliver an effective, specific solution
- The importance of simple UI in providing a satisfying UX
- Getting important features done first before spending time on less important details
- Getting clear communication between front end & back end to ensure everyone has the same understanding of functionality before splitting into groups

## What's next for MySOP
- Consider more potential risks and issues before settling on an idea
- Better UX via:
  - Better searching function
  - Algorithm to recommend content to users based on tags they have followed/engaged with before
- More efficient method to gather latest SOP details
  - Web-scraper or partnership with government sources (MKN)
	 



