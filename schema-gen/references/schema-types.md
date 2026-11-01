# Schema Types Quick Reference

Required (R) and Recommended (Rec) properties per schema type. Based on Google's structured data documentation and Schema.org specs.

---

## Organization

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Organization" or more specific subtype |
| name | R | Text | Official organization name |
| url | R | URL | Homepage URL |
| logo | Rec | ImageObject | Min 112x112px, square preferred |
| description | Rec | Text | One sentence |
| foundingDate | Rec | Date | Year or ISO date |
| founder | Rec | Person | Nested Person object |
| sameAs | Rec | URL[] | Social profiles, Wikipedia, Wikidata |
| contactPoint | Rec | ContactPoint | Email or phone with contactType |
| address | Rec | PostalAddress | Physical address if applicable |

---

## WebSite

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "WebSite" |
| name | R | Text | Site name |
| url | R | URL | Homepage |
| potentialAction | Rec | SearchAction | Only if site has search functionality |

### SearchAction (nested in WebSite)

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "SearchAction" |
| target | R | EntryPoint | urlTemplate with {search_term_string} |
| query-input | R | Text | "required name=search_term_string" |

---

## Article

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Article", "NewsArticle", or "BlogPosting" |
| headline | R | Text | Max 110 characters |
| image | R | ImageObject/URL | Min 1200px wide, 16:9 or 4:3 or 1:1 |
| datePublished | R | DateTime | ISO 8601 |
| dateModified | Rec | DateTime | ISO 8601, update on every edit |
| author | R | Person/Organization | Nested with name and url |
| publisher | Rec | Organization | With name and logo |
| description | Rec | Text | Meta description |
| mainEntityOfPage | Rec | WebPage | @id = canonical URL |
| wordCount | Rec | Integer | Approximate word count |
| keywords | Rec | Text[] | Array of relevant keywords |
| articleSection | Rec | Text | Category name |
| inLanguage | Rec | Text | BCP 47 language code |

---

## FAQPage

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "FAQPage" |
| mainEntity | R | Question[] | Array of Question objects |

### Question (nested in FAQPage)

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Question" |
| name | R | Text | The question text |
| acceptedAnswer | R | Answer | Single Answer object |

### Answer (nested in Question)

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Answer" |
| text | R | Text | Full answer, HTML allowed |

---

## HowTo

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "HowTo" |
| name | R | Text | Title of the how-to |
| step | R | HowToStep[] | Array of steps |
| description | Rec | Text | Brief summary |
| totalTime | Rec | Duration | ISO 8601 duration (PT30M) |
| estimatedCost | Rec | MonetaryAmount | Cost to complete |
| supply | Rec | HowToSupply[] | Required materials |
| tool | Rec | HowToTool[] | Required tools |
| image | Rec | ImageObject/URL | Hero image |

### HowToStep

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "HowToStep" |
| text | R | Text | Step instructions |
| name | Rec | Text | Step title |
| url | Rec | URL | Anchor link to step |
| image | Rec | ImageObject/URL | Step screenshot |

---

## Product

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Product" |
| name | R | Text | Product name |
| image | R | ImageObject/URL | Product image |
| description | Rec | Text | Product description |
| brand | Rec | Brand | Brand name |
| sku | Rec | Text | Unique identifier |
| gtin | Rec | Text | Global Trade Item Number |
| offers | R | Offer | Pricing info |
| aggregateRating | Rec | AggregateRating | Only with real reviews |
| review | Rec | Review[] | Individual reviews |

### Offer (nested in Product)

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Offer" |
| price | R | Text | Price as string ("49.00") |
| priceCurrency | R | Text | ISO 4217 (USD, EUR, etc.) |
| availability | R | URL | Schema.org/InStock, OutOfStock, etc. |
| url | Rec | URL | Product page URL |
| priceValidUntil | Rec | Date | Expiry date for price |
| seller | Rec | Organization | Seller info |

---

## LocalBusiness

Inherits all Organization properties plus:

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "LocalBusiness" or specific subtype |
| name | R | Text | Business name |
| address | R | PostalAddress | Full address |
| telephone | Rec | Text | Phone number |
| geo | Rec | GeoCoordinates | Latitude/longitude |
| openingHoursSpecification | Rec | OpeningHoursSpecification[] | Business hours |
| priceRange | Rec | Text | "$" to "$$$$" |
| image | Rec | ImageObject/URL | Storefront or logo |
| servesCuisine | Rec | Text | Restaurant only |
| menu | Rec | URL | Restaurant only |

**Specific subtypes:** Restaurant, Dentist, LegalService, RealEstateAgent, MedicalBusiness, AutomotiveBusiness, FinancialService, FoodEstablishment, HealthAndBeautyBusiness, HomeAndConstructionBusiness, LodgingBusiness, Store, SportsActivityLocation

---

## Person

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Person" |
| name | R | Text | Full name |
| url | Rec | URL | Profile/author page |
| image | Rec | ImageObject/URL | Photo |
| jobTitle | Rec | Text | Current role |
| worksFor | Rec | Organization | Employer |
| description | Rec | Text | Short bio |
| sameAs | Rec | URL[] | Social profiles |
| knowsAbout | Rec | Text[] | Areas of expertise |
| alumniOf | Rec | Organization | Education |

---

## BreadcrumbList

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "BreadcrumbList" |
| itemListElement | R | ListItem[] | Ordered breadcrumb items |

### ListItem

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "ListItem" |
| position | R | Integer | 1-based index |
| name | R | Text | Display text |
| item | R* | URL | Page URL (*omit on last item) |

---

## VideoObject

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "VideoObject" |
| name | R | Text | Video title |
| description | R | Text | Video description |
| thumbnailUrl | R | URL | Thumbnail image |
| uploadDate | R | DateTime | ISO 8601 |
| duration | Rec | Duration | ISO 8601 (PT10M30S) |
| contentUrl | Rec | URL | Direct video file URL |
| embedUrl | Rec | URL | Embeddable URL (YouTube embed) |
| publisher | Rec | Organization | Channel/publisher |
| interactionStatistic | Rec | InteractionCounter | View count |

---

## Event

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Event" or subtype |
| name | R | Text | Event name |
| startDate | R | DateTime | ISO 8601 with timezone |
| location | R | Place/VirtualLocation | Venue or URL |
| description | Rec | Text | Event description |
| endDate | Rec | DateTime | ISO 8601 |
| eventStatus | Rec | URL | EventScheduled, EventCancelled, etc. |
| eventAttendanceMode | Rec | URL | OnlineEventAttendanceMode, OfflineEventAttendanceMode, MixedEventAttendanceMode |
| organizer | Rec | Organization/Person | Event organizer |
| offers | Rec | Offer | Ticket info |
| performer | Rec | Person/Organization | Speakers/performers |
| image | Rec | ImageObject/URL | Event banner |

---

## Course

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Course" |
| name | R | Text | Course title |
| description | R | Text | Course description |
| provider | R | Organization | Who offers the course |
| offers | Rec | Offer | Pricing |
| hasCourseInstance | Rec | CourseInstance | Delivery details |
| educationalLevel | Rec | Text | Beginner/Intermediate/Advanced |
| about | Rec | Text[] | Topics covered |
| inLanguage | Rec | Text | BCP 47 code |
| totalHistoricalEnrollment | Rec | Integer | Number of students |

---

## SoftwareApplication

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "SoftwareApplication" or "WebApplication" |
| name | R | Text | App name |
| offers | R | Offer | Pricing (use "0" for free) |
| applicationCategory | Rec | Text | BusinessApplication, GameApplication, etc. |
| operatingSystem | Rec | Text | "Web", "Windows", "macOS", "iOS", "Android" |
| description | Rec | Text | App description |
| screenshot | Rec | ImageObject/URL | App screenshot |
| aggregateRating | Rec | AggregateRating | Only with real reviews |
| author | Rec | Organization/Person | Developer |
| softwareVersion | Rec | Text | Current version |
| downloadUrl | Rec | URL | Direct download link |

---

## AggregateRating (reusable component)

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "AggregateRating" |
| ratingValue | R | Number/Text | Average rating |
| ratingCount | R | Integer | Total number of ratings |
| bestRating | Rec | Number/Text | Max possible (default 5) |
| worstRating | Rec | Number/Text | Min possible (default 1) |
| reviewCount | Rec | Integer | Ratings with written reviews |

---

## Review (reusable component)

| Property | Status | Type | Notes |
|----------|--------|------|-------|
| @type | R | Text | "Review" |
| author | R | Person | Reviewer |
| reviewRating | R | Rating | Star rating |
| datePublished | Rec | Date | When review was written |
| reviewBody | Rec | Text | Review text |

---

## ISO 8601 Duration Reference

| Format | Meaning |
|--------|---------|
| PT30M | 30 minutes |
| PT1H30M | 1 hour 30 minutes |
| PT10H | 10 hours |
| P1D | 1 day |
| P7D | 7 days |
| PT2M30S | 2 minutes 30 seconds |
