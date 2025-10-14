# UI/UX and Non-Functional Requirements

## Activity 1: Personas & Scenarios

### Persona 1: Sarah Williams – The Customer

**Age:** 34  
**Occupation:** Bank Customer (NatWest)  
**Location:** London, UK  
**Quote:** "When something goes wrong with my account, I just want it fixed quickly and easily."

**Goals:**
- Report issues like false transactions or blocked cards easily
- Track complaint progress online without calling support
- Receive timely updates and confirmations

**Frustrations:**
- Long wait times on calls
- Unclear complaint status information
- Having to repeat details to multiple agents

**Technology:** Uses a smartphone and laptop regularly; prefers mobile apps and self-service portals

**Scenario:** Sarah notices an unauthorized debit card transaction. She logs into the CMS mobile app, reports the issue, uploads a screenshot, and receives an instant case number. She later gets a push notification confirming that the support team has resolved the issue and that her card has been reissued.

### Persona 2: James Patel – The Help Desk Agent

**Age:** 41  
**Occupation:** Help Desk Agent (Vodafone)  
**Location:** Birmingham, UK  
**Quote:** "The faster I can resolve each case, the happier my customers are."

**Goals:**
- Log complaints from customers efficiently
- Assign issues to the right support staff based on category
- Provide regular updates to customers

**Frustrations:**
- Slow or unresponsive system interfaces
- Inability to easily search for existing cases
- Lack of automated suggestions for resolution steps

**Technology:** Primarily works on a desktop system at the call centre; comfortable with enterprise web interfaces

**Scenario:** James answers a call from a customer reporting no mobile network. He quickly logs the issue in the CMS, checks previous linked complaints, and assigns the case to the network engineer. He later sends an update to the customer once the issue is marked as resolved.

## Activity 2: Mapping to Non-Functional Requirements

### Persona: Sarah Williams

**Scenario Summary:** Customer uses CMS mobile app to report unauthorized card transaction and track status

**Relevant NFRs:** Performance, Usability, Reliability, Security

**Why Important?** The app must respond quickly (Performance) and have a simple complaint reporting UI (Usability) for a stress-free experience. Consistently notifying users about progress (Reliability) builds trust, while handling sensitive financial data securely (Security) is essential.

### Persona: James Patel

**Scenario Summary:** Agent uses CMS desktop portal to log and assign customer complaints efficiently

**Relevant NFRs:** Usability, Availability, Reliability

**Why Important?** A clear, fast interface (Usability) enables efficient call handling during busy shifts. System uptime (Availability) ensures continuous service for both agents and customers, while reliability ensures smooth workflow and accurate updates.

## Activity 3: Storyboarding the Experience

### Sarah Williams's Storyboard (Mobile-First Experience)

**Step 1:** Sarah opens the CMS app on her phone and logs in instantly with Face ID  
*NFRs: Performance & Security – The login is fast ("instantly") and uses a secure, convenient method (Face ID)*

**Step 2:** She taps "Report a Problem" and selects "False Transaction" from clear, categorized options  
*NFRs: Usability – The interface provides intuitive problem categories that are easy to navigate*

**Step 3:** She enters transaction details, adds a comment, and uploads a screenshot as evidence  
*NFRs: Usability & Performance – The form is straightforward, and the upload process is quick and responsive*

**Step 4:** She receives an instant case number and an estimated resolution timeframe on the confirmation screen  
*NFRs: Reliability – Immediate system confirmation provides assurance that her complaint has been logged successfully*

**Step 5:** Later that day, she receives a push notification confirming the issue is resolved and her card is being reissued  
*NFRs: Reliability & Security – The system reliably delivers important status updates about sensitive account changes*

### James Patel's Storyboard (Web-Based Workflow)

**Step 1:** James logs into the CMS web dashboard at the start of his shift  
*NFRs: Availability – The system must be consistently available during operational hours*

**Step 2:** He receives a customer call and searches for the customer's previous complaint history by phone number  
*NFRs: Performance – Quick search and data retrieval are essential for efficient call handling*

**Step 3:** He logs a new "No Network" complaint using the quick-entry form with dropdown categories  
*NFRs: Usability – Efficient form design with pre-set options enables rapid data entry*

**Step 4:** He assigns the case to a network technician and adds initial troubleshooting notes  
*NFRs: Reliability – The system must accurately save assignment data and notes for traceability*

**Step 5:** He updates the customer record with a summary of the call and next steps  
*NFRs: Usability & Reliability – Clear data entry fields and reliable saving ensure accurate case documentation*

**Step 6:** The system shows a confirmation message and the case appears in his "Active Cases" dashboard  
*NFRs: Reliability – Consistent system feedback confirms successful completion of each action*

## Activity 4: Group Reflection

**Feedback Notes:**

The storyboards clearly differentiate between a mobile-focused customer experience (Sarah) and a desktop-based agent workflow (James). Sarah's flow effectively highlights the need for Performance and Usability in a consumer-facing app, while James's story emphasizes Availability and Reliability for internal users.
