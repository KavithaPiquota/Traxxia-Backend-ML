# Langfuse Integration Guide

## Overview
This application now includes Langfuse observability for tracking OpenAI API usage, token consumption, costs, and performance metrics.

## What's Integrated
- **Automatic tracking** of all OpenAI API calls across all endpoints
- **Token usage monitoring** (prompt tokens, completion tokens, total tokens)
- **Cost calculation** per API call and session
- **Session tracking** to group related API calls
- **User identification** for client-specific monitoring
- **Model tracking** (gpt-4o, gpt-4o-mini, etc.)
- **Latency monitoring** for performance analysis

## Setup

### 1. Environment Variables
Add these to your `.env` file:

```bash
LANGFUSE_SECRET_KEY=sk-lf-da6c7de3-7480-49f3-8fbb-7c0e376827ee
LANGFUSE_PUBLIC_KEY=pk-lf-910b453b-f5b4-47c9-86f3-c8ffbf70c7ca
LANGFUSE_HOST=https://cloud.langfuse.com
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## How It Works

### Automatic Tracking
All OpenAI API calls are automatically tracked without any code changes to your endpoints. The integration uses Langfuse's OpenAI wrapper which is a drop-in replacement for the standard OpenAI client.

### Session Tracking
Clients can send session information via HTTP headers:

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -H "X-Session-ID: session_abc123" \
  -H "X-User-ID: client_xyz" \
  -d '{"question": "What is the revenue?", "answer": "$1M"}'
```

**Headers:**
- `X-Session-ID`: Groups multiple API calls into a single session
- `X-User-ID`: Identifies the client/user making the request

**If headers are not provided:**
- Session ID is auto-generated from the client's IP address
- User ID defaults to "anonymous"

## What Gets Tracked

For each OpenAI API call, Langfuse tracks:

1. **Input/Output**
   - Full prompt/messages sent to OpenAI
   - Complete response received

2. **Token Usage**
   - Prompt tokens
   - Completion tokens
   - Total tokens

3. **Cost**
   - Automatically calculated based on model pricing
   - Per-call and aggregated costs

4. **Performance**
   - Response latency
   - API call duration

5. **Context**
   - Model used (gpt-4o, gpt-4o-mini, etc.)
   - Temperature, max_tokens, and other parameters
   - Session ID and User ID
   - Endpoint name

## Viewing Data in Langfuse

1. Go to https://cloud.langfuse.com
2. Log in with your credentials
3. View dashboards for:
   - **Sessions**: See all API calls grouped by session
   - **Users**: Track usage per client
   - **Models**: Compare performance across different models
   - **Costs**: Monitor token consumption and costs
   - **Traces**: Debug individual API calls with full input/output

## Example Session View

```
Session: session_abc123
User: client_xyz
Duration: 8.5 seconds
Total Calls: 5
Total Tokens: 1,250
Total Cost: $0.015

Calls:
1. POST /analyze - gpt-4o - 200 tokens - $0.003 - 1.2s
2. POST /analyze - gpt-4o - 180 tokens - $0.0027 - 1.1s
3. POST /customer-segment - gpt-4o - 350 tokens - $0.0053 - 2.1s
4. POST /full-swot-portfolio - gpt-4o - 420 tokens - $0.0063 - 2.8s
5. POST /full-swot-portfolio - gpt-4o - 100 tokens - $0.0015 - 1.3s
```

## Benefits

✅ **Zero code changes** to existing endpoints
✅ **Automatic tracking** of all OpenAI calls
✅ **Session-based monitoring** for client usage patterns
✅ **Cost transparency** for billing and budgeting
✅ **Performance insights** for optimization
✅ **Debugging support** with full input/output logs
✅ **Model comparison** to optimize costs vs. quality

## Notes

- **Perplexity API calls** are NOT tracked (as requested)
- All tracking happens transparently in the background
- No impact on API response times or functionality
- Data is securely stored in Langfuse cloud
