# JobLink - Complete Webflow Design Brief

## Project Overview
**JobLink** is a modern service marketplace platform connecting clients with verified service providers in Kenya. The platform combines the functionality of TaskRabbit and Upwork with local M-Pesa integration and Kenyan-specific features.

**Target Audience**: Kenyan service seekers and service providers
**Platform Type**: Two-sided marketplace
**Key Features**: Service booking, provider verification, M-Pesa payments, reviews

---

## Design System

### Color Palette
```
Primary Colors:
- Primary Blue: #2563eb
- Primary Light: #3b82f6  
- Primary Dark: #1d4ed8
- Primary Background: #eff6ff

Secondary Colors:
- Purple Accent: #7c3aed
- Success Green: #10b981
- Warning Orange: #f59e0b
- Error Red: #ef4444

Kenya-Specific:
- M-Pesa Green: #00a86b
- Safaricom Red: #e60000

Neutral Colors:
- Gray 50: #f9fafb (light backgrounds)
- Gray 100: #f3f4f6 (card backgrounds)
- Gray 200: #e5e7eb (borders)
- Gray 500: #6b7280 (secondary text)
- Gray 700: #374151 (primary text)
- Gray 900: #111827 (headings)
```

### Typography
```
Font Family: Inter (Google Fonts)

Font Sizes:
- H1 (Hero): 48px / Bold
- H2 (Page Titles): 36px / Bold  
- H3 (Section Headers): 24px / Semibold
- H4 (Card Titles): 20px / Semibold
- Body Large: 18px / Regular
- Body: 16px / Regular
- Body Small: 14px / Regular
- Caption: 12px / Medium
```

### Component Specifications

#### Buttons
```
Primary Button:
- Background: #2563eb
- Text: White, 16px, Medium weight
- Padding: 12px 24px
- Border Radius: 8px
- Hover: Background #1d4ed8
- Height: 48px (large), 40px (medium), 32px (small)

Secondary Button:
- Background: Transparent
- Border: 2px solid #2563eb
- Text: #2563eb, 16px, Medium weight
- Hover: Background #eff6ff
- Same sizing as primary
```

#### Cards
```
Standard Card:
- Background: White
- Border Radius: 12px
- Shadow: 0 4px 6px rgba(0,0,0,0.1)
- Padding: 24px
- Hover: Shadow 0 8px 25px rgba(0,0,0,0.15)

Provider Card:
- Size: 320px × 400px
- Image Area: 320px × 200px (top)
- Content Padding: 20px
- Hover: Lift effect with increased shadow
```

#### Form Elements
```
Input Fields:
- Height: 48px
- Border: 1px solid #d1d5db
- Border Radius: 8px
- Padding: 12px 16px
- Focus: Border #2563eb, Ring 2px #eff6ff
- Font: 16px Regular

Select Dropdowns:
- Same styling as inputs
- Chevron icon on right
- Options: White background, hover #f3f4f6
```

---

## Page Layouts

### 1. Homepage

#### Hero Section
```
Layout: Full viewport height (100vh)
Background: Linear gradient from #2563eb to #7c3aed (diagonal)
Content: Centered, max-width 1200px

Elements:
- Main Headline: "Find Your Perfect Service Provider"
  - Font: 48px Bold, White
  - Line height: 1.2
  - Margin bottom: 16px

- Subheadline: "Connect with trusted professionals in your area. Book services, read reviews, and get the job done right."
  - Font: 24px Regular, rgba(255,255,255,0.9)
  - Max width: 600px
  - Margin bottom: 32px

- CTA Buttons (flex row, gap 16px):
  - "Find Services": Yellow background #fbbf24, dark text
  - "Join as Provider": White border, white text
  - Both: 48px height, 24px padding horizontal

- Floating Elements:
  - Yellow circle: 80px diameter, top-left, animate bounce
  - Purple circle: 64px diameter, bottom-right, animate pulse
```

#### Service Categories Section
```
Layout: Container max-width 1200px, padding 80px vertical
Background: White

Header:
- "Popular Services" (36px Bold, centered)
- "Find the perfect service for your needs" (18px, gray, centered)
- Margin bottom: 48px

Grid:
- Desktop: 6 columns
- Tablet: 3 columns  
- Mobile: 2 columns
- Gap: 24px

Category Cards:
- Background: White
- Size: Auto height, equal width
- Padding: 24px
- Border radius: 16px
- Shadow: 0 2px 8px rgba(0,0,0,0.1)
- Hover: Transform translateY(-4px), shadow increase

Card Content:
- Icon: 64px emoji, centered
- Title: 18px Semibold, margin top 16px
- Count: 14px Gray, margin top 4px

Services:
1. Cleaning 🧹 (120+ providers)
2. Plumbing 🔧 (85+ providers)
3. Electrical ⚡ (95+ providers)
4. Gardening 🌱 (70+ providers)
5. Beauty 💄 (110+ providers)
6. IT Support 💻 (60+ providers)
7. Painting 🎨 (45+ providers)
8. Catering 🍽️ (55+ providers)
9. Photography 📸 (40+ providers)
10. Tutoring 📚 (80+ providers)
11. Handyman 🔨 (90+ providers)
12. Carpentry 🪚 (35+ providers)
```

#### How It Works Section
```
Layout: Container max-width 1200px, padding 80px vertical
Background: #f9fafb

Header: Same styling as categories section
Title: "How JobLink Works"
Subtitle: "Get connected with trusted service providers in 3 simple steps"

Grid: 3 columns (stack on mobile)
Gap: 48px

Step Cards:
- Text align: center
- No background (transparent)

Step Elements:
- Number Circle: 80px diameter, colored background, white number
  - Step 1: #2563eb, Step 2: #10b981, Step 3: #7c3aed
- Title: 24px Semibold, margin top 24px
- Description: 16px Regular, gray, margin top 12px, max-width 280px

Steps:
1. "Search & Browse" - Browse verified providers and read reviews
2. "Book & Schedule" - Select provider, choose time, book service  
3. "Pay & Review" - Pay securely and leave feedback
```

#### Statistics Section
```
Layout: Full width, padding 80px vertical
Background: Linear gradient #2563eb to #7c3aed
Text: White, centered

Header:
- "Trusted by Thousands" (36px Bold)
- "Join our growing community" (18px, opacity 0.9)
- Margin bottom: 48px

Stats Grid: 4 columns (2x2 on mobile)
Gap: 48px

Stat Items:
- Number: 48px Bold
- Label: 16px Regular, opacity 0.8
- Margin between: 8px

Statistics:
- 500+ (Verified Providers)
- 2,000+ (Happy Customers)  
- 5,000+ (Services Completed)
- 4.8★ (Average Rating)
```

#### Testimonials Section
```
Layout: Container max-width 1200px, padding 80px vertical
Background: White

Header: "What Our Customers Say"
Grid: 3 columns (stack on mobile)

Testimonial Cards:
- Background: #f9fafb
- Padding: 32px
- Border radius: 16px
- Gap: 32px

Card Elements:
- Star Rating: 5 yellow stars (20px each)
- Quote: 16px Regular, line height 1.6, margin 16px vertical
- Avatar: 48px circle, colored background with initial
- Name: 16px Semibold
- Location: 14px Gray

Sample Testimonials:
1. Mary W. (Nairobi) - "Amazing plumber service, very professional"
2. John K. (Kiambu) - "Great electrician, fair pricing, excellent work"  
3. Anne M. (Mombasa) - "Reliable platform, always professional providers"
```

### 2. Provider Listing Page

#### Search Section
```
Layout: Full width, white background, padding 32px vertical
Shadow: 0 2px 4px rgba(0,0,0,0.1)

Search Container: Max-width 1200px, centered

Main Search Bar:
- Flex layout, gap 16px
- Keyword input: Flex 1, "What service do you need?"
- Location input: 300px width, "Location"  
- Search button: Primary blue, "Search"
- Filters button: Secondary, "Filters" with icon

Advanced Filters (collapsible):
- Grid: 3 columns
- Category dropdown, Price range (dual slider), Rating filter
- Availability, Distance, "Verified only" checkbox
- Apply/Clear buttons
```

#### Provider Grid
```
Layout: Container max-width 1200px
Grid: 3 columns desktop, 2 tablet, 1 mobile
Gap: 32px
Padding: 48px vertical

Provider Cards:
- Size: 320px width, auto height
- Background: White
- Border radius: 12px
- Shadow: 0 4px 6px rgba(0,0,0,0.1)
- Hover: Shadow increase, translateY(-2px)

Card Structure:
- Image: 320px × 200px, object-fit cover
- Content padding: 20px
- Name: 20px Semibold
- Service: 16px Medium, blue color
- Location: 14px Gray with map pin icon
- Description: 14px Regular, 2 lines max
- Verification badges: Small colored pills
- Rating: Stars + number
- Price: Large, bold, "/hr"
- Book button: Full width, primary
```

### 3. Client Dashboard

#### Header
```
Layout: Full width, white background, border bottom
Padding: 24px vertical
Content: Max-width 1200px, flex justify-between

Left Side:
- "Welcome back, [Name]!" (24px Bold)
- "Manage your bookings and find new services" (16px Gray)

Right Side:
- "Book New Service" button (primary, with plus icon)
```

#### Stats Cards
```
Layout: Grid 3 columns, gap 24px, margin 32px vertical

Card Structure:
- Background: White
- Padding: 24px
- Border radius: 12px
- Shadow: 0 2px 8px rgba(0,0,0,0.1)

Card Elements:
- Icon: 48px colored background circle
- Number: 32px Bold
- Label: 14px Gray

Stats:
1. Total Bookings (Calendar icon, blue)
2. Average Rating Given (Star icon, yellow)
3. Total Spent (Credit card icon, green)
```

#### Recent Bookings
```
Layout: White card, padding 32px
Title: "Recent Bookings" with "View All" link

Booking Items:
- Border: Light gray bottom border
- Padding: 20px vertical
- Flex layout

Item Elements:
- Service name: 18px Semibold
- Provider: 16px Regular with "Provider:" prefix
- Date/time: 14px Gray with calendar icon
- Location: 14px Gray with map icon
- Amount: 16px Bold with "KSh" prefix
- Status badge: Colored pill (blue/green/yellow)
```

### 4. Provider Dashboard

#### Header
```
Layout: Full width, gradient background (#10b981 to #2563eb)
Padding: 48px vertical
Text: White

Content: Max-width 1200px, flex layout
Left: Business info, verification badges
Right: Rating display, edit button

Elements:
- Business name: 32px Bold
- Experience: 18px Regular, opacity 0.9
- Verification badges: Colored pills
- Rating: Large stars with number
```

#### Business Stats
```
Layout: Grid 4 columns, gap 24px
Cards: Same styling as client dashboard

Stats:
1. Total Bookings (blue)
2. Monthly Earnings (green)  
3. Average Rating (yellow)
4. Happy Clients (purple)
```

#### Portfolio Section
```
Layout: White card, padding 32px
Header: "Portfolio" with "Add Work" button

Grid: 2 columns, gap 24px

Portfolio Items:
- Image placeholder: 300px × 200px, gray background
- Title: 18px Semibold
- Description: 14px Regular
- Border radius: 8px
```

### 5. Reviews Page

#### Header
```
Layout: Gradient background, padding 64px vertical
Content: Centered, white text

Elements:
- Title: "Customer Reviews" (36px Bold)
- Subtitle: "See what customers say about JobLink providers"
- Overall rating: Large stars with average number
- Total reviews count
```

#### Review Cards
```
Layout: Single column, gap 24px
Card: White background, padding 24px, border radius 12px

Card Elements:
- Customer avatar: 48px circle with initial
- Name and service: 18px Semibold
- Star rating: 5 stars, colored
- Review text: 16px Regular, line height 1.6
- Date: 14px Gray
- Helpful button: Small, secondary
```

---

## Kenya-Specific Features

### M-Pesa Integration
```
Visual Elements:
- M-Pesa logo: Green circle with white "M"
- Payment cards: Green accent color
- Phone input: +254 prefix, Kenya flag icon
- Success states: Green color scheme

Payment Flow:
- Payment method selection
- Phone number input with validation
- Amount confirmation
- Success/failure states
```

### Local Adaptations
```
Currency: KSh prefix for all amounts
Phone Format: +254 XXX XXX XXX
Locations: Nairobi, Mombasa, Kisumu, Nakuru dropdowns
Services: Kenya-relevant categories
Language: English with Swahili option toggle
```

---

## Interactive Elements

### Hover States
```
Buttons: Darken by 10%, smooth transition
Cards: Lift effect (translateY -2px to -4px)
Links: Color change + underline
Images: Slight scale (1.05x)
```

### Loading States
```
Skeleton screens: Gray placeholders with shimmer
Spinners: Primary blue, 24px diameter
Progress bars: Blue fill, gray background
```

### Form Validation
```
Success: Green border + checkmark icon
Error: Red border + error message below
Focus: Blue border + subtle glow
Required: Red asterisk
```

### Status Indicators
```
Confirmed: Blue background, white text
Pending: Yellow background, dark text  
Completed: Green background, white text
Cancelled: Red background, white text
```

---

## Responsive Breakpoints

### Mobile (320px - 767px)
```
Navigation: Hamburger menu, slide-out drawer
Grids: Single column layouts
Buttons: Full width where appropriate
Text: Slightly smaller font sizes
Spacing: Reduced padding/margins
Touch targets: Minimum 44px
```

### Tablet (768px - 1023px)  
```
Grids: 2-column layouts
Navigation: Horizontal with some items hidden
Mixed layouts: Some single, some multi-column
```

### Desktop (1024px+)
```
Full multi-column layouts
Hover effects enabled
Maximum content widths: 1200px
Generous spacing and padding
```

---

## Technical Requirements

### Performance
```
Images: WebP format, lazy loading
Animations: CSS transitions, 60fps
Loading: Under 3 seconds
Optimization: Minified CSS/JS
```

### Accessibility
```
Contrast: WCAG AA compliance (4.5:1 minimum)
Navigation: Keyboard accessible
Screen readers: Proper ARIA labels
Focus: Visible focus indicators
Alt text: All images described
```

### SEO
```
Semantic HTML: Proper heading hierarchy
Meta tags: Title, description, keywords
Schema markup: Local business, reviews
Clean URLs: Descriptive, no parameters
Sitemap: XML sitemap included
```

---

## Content Guidelines

### Tone of Voice
```
Professional yet approachable
Trustworthy and reliable
Clear and concise
Locally relevant
Inclusive and welcoming
```

### Key Messages
```
Trust: "Verified providers you can trust"
Convenience: "Book services in minutes"
Local: "Supporting Kenyan businesses"
Quality: "Quality services, guaranteed"
Security: "Secure payments with M-Pesa"
```

### Call-to-Actions
```
Primary: "Find Services", "Book Now", "Get Started"
Secondary: "Learn More", "View Profile", "See Reviews"
Provider: "Join as Provider", "Start Earning"
```

This comprehensive design brief provides all the specifications needed to recreate the JobLink platform in Webflow with professional design standards and Kenya-specific functionality.