#!/usr/bin/env python3
"""
Test script for SWOT Analysis functionality
"""

import os
from dotenv import load_dotenv
from swot_analysis import SWOTNewsAnalyzer

load_dotenv()

def test_swot_analyzer():
    """Test the SWOT analyzer with a simple company"""
    
    # Get API key from environment
    api_key = os.getenv("NEWSAPI_API_KEY")
    
    if not api_key:
        print("❌ NEWSAPI_API_KEY not found in environment variables")
        print("Please add your NewsAPI key to the .env file")
        return False
    
    print("🔍 Testing SWOT Analysis...")
    
    # Initialize analyzer
    analyzer = SWOTNewsAnalyzer(api_key)
    
    # Test with a well-known company
    test_company = "Tesla"
    
    print(f"📊 Analyzing {test_company}...")
    
    try:
        # Generate SWOT analysis
        swot_data = analyzer.generate_swot_analysis(test_company, days_back=7)
        
        if swot_data:
            print("✅ SWOT analysis generated successfully!")
            
            # Print summary
            print(f"\n📈 Results for {test_company}:")
            print(f"   Strengths: {len(swot_data['strengths'])} articles")
            print(f"   Weaknesses: {len(swot_data['weaknesses'])} articles")
            print(f"   Opportunities: {len(swot_data['opportunities'])} articles")
            print(f"   Threats: {len(swot_data['threats'])} articles")
            
            # Test report generation
            report = analyzer.generate_swot_report(swot_data, test_company)
            print(f"\n📄 Report generated: {len(report)} characters")
            
            # Show a sample of the report
            print("\n📋 Sample report (first 500 characters):")
            print("-" * 50)
            print(report[:500] + "..." if len(report) > 500 else report)
            
            return True
        else:
            print("❌ Failed to generate SWOT analysis")
            return False
            
    except Exception as e:
        print(f"❌ Error during SWOT analysis: {e}")
        return False

def test_categorization():
    """Test the article categorization functionality"""
    print("\n🏷️  Testing article categorization...")
    
    api_key = os.getenv("NEWSAPI_API_KEY", "dummy_key")
    analyzer = SWOTNewsAnalyzer(api_key)
    
    # Test cases
    test_cases = [
        ("Company reports record profits and growth", "Strong quarterly results", "strengths"),
        ("Company faces lawsuit and declining sales", "Legal troubles continue", "weaknesses"),
        ("New market opportunities emerge in Asia", "Expansion potential identified", "opportunities"),
        ("Increased competition threatens market share", "Rivals gaining ground", "threats"),
        ("Regular business update", "Standard operations continue", "neutral")
    ]
    
    print("Testing categorization with sample articles:")
    for title, description, expected in test_cases:
        category = analyzer.categorize_article(title, description)
        status = "✅" if category == expected else "❌"
        print(f"  {status} '{title[:30]}...' → {category} (expected: {expected})")

if __name__ == "__main__":
    print("🧪 SWOT Analysis Test Suite")
    print("=" * 50)
    
    # Test categorization logic
    test_categorization()
    
    # Test full SWOT analysis
    success = test_swot_analyzer()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ All tests passed! SWOT analysis is working correctly.")
    else:
        print("❌ Some tests failed. Please check your API key and internet connection.")
