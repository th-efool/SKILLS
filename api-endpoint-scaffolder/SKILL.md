\---

name: api-endpoint-scaffolder

description: Generate REST API endpoints with proper structure, validation, error handling, and types. Use when creating new API routes, endpoints, or backend services.

\---



\# API Endpoint Scaffolder



\## Instructions



When creating a new API endpoint:



1\. \*\*Identify the framework\*\* (Express, Next.js, FastAPI, etc.)

2\. \*\*Determine HTTP method\*\* (GET, POST, PUT, PATCH, DELETE)

3\. \*\*Define request/response types\*\*

4\. \*\*Implement with best practices\*\*



\## Templates



\### Next.js App Router (TypeScript)



```typescript

// app/api/\[resource]/route.ts

import { NextRequest, NextResponse } from 'next/server';

import { z } from 'zod';



const RequestSchema = z.object({

&#x20; // Define your schema

});



export async function GET(request: NextRequest) {

&#x20; try {

&#x20;   const { searchParams } = new URL(request.url);

&#x20;   // Implementation

&#x20;   return NextResponse.json({ data }, { status: 200 });

&#x20; } catch (error) {

&#x20;   console.error('\[API] Error:', error);

&#x20;   return NextResponse.json(

&#x20;     { error: 'Internal server error' },

&#x20;     { status: 500 }

&#x20;   );

&#x20; }

}



export async function POST(request: NextRequest) {

&#x20; try {

&#x20;   const body = await request.json();

&#x20;   const validated = RequestSchema.parse(body);

&#x20;   // Implementation

&#x20;   return NextResponse.json({ data }, { status: 201 });

&#x20; } catch (error) {

&#x20;   if (error instanceof z.ZodError) {

&#x20;     return NextResponse.json(

&#x20;       { error: 'Validation failed', details: error.errors },

&#x20;       { status: 400 }

&#x20;     );

&#x20;   }

&#x20;   return NextResponse.json(

&#x20;     { error: 'Internal server error' },

&#x20;     { status: 500 }

&#x20;   );

&#x20; }

}

```



\### Express (TypeScript)



```typescript

import { Router, Request, Response, NextFunction } from 'express';

import { z } from 'zod';



const router = Router();



const CreateSchema = z.object({

&#x20; // Define schema

});



router.post('/', async (req: Request, res: Response, next: NextFunction) => {

&#x20; try {

&#x20;   const data = CreateSchema.parse(req.body);

&#x20;   // Implementation

&#x20;   res.status(201).json({ success: true, data });

&#x20; } catch (error) {

&#x20;   next(error);

&#x20; }

});



export default router;

```



\## Best Practices



1\. \*\*Always validate input\*\* using Zod, Yup, or similar

2\. \*\*Use proper HTTP status codes\*\*:

&#x20;  - 200: Success

&#x20;  - 201: Created

&#x20;  - 400: Bad Request

&#x20;  - 401: Unauthorized

&#x20;  - 403: Forbidden

&#x20;  - 404: Not Found

&#x20;  - 500: Server Error

3\. \*\*Log errors\*\* but don't expose internals to clients

4\. \*\*Use consistent response format\*\*

5\. \*\*Add rate limiting\*\* for public endpoints

6\. \*\*Document with OpenAPI/Swagger\*\* when possible



