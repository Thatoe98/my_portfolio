"""
ATS-Optimized Resume Generator
Creates a one-page PDF resume that is ATS-friendly
Uses standard formatting, simple layout, no tables or complex elements
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import datetime
import os

class HorizontalLine(Flowable):
    """Custom horizontal line for section separators"""
    def __init__(self, width, color=colors.black, thickness=0.5):
        Flowable.__init__(self)
        self.width = width
        self.color = color
        self.thickness = thickness

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)

def create_resume():
    """Generate ATS-optimized resume PDF"""
    
    # Create PDF
    filename = f"Thatoe_Nyi_Resume_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Container for elements
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles for ATS optimization - COMPACT VERSION
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=1,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        spaceAfter=2,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#444444'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=10,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=2,
        spaceBefore=3,
        fontName='Helvetica-Bold',
        textTransform='uppercase'
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=0,
        fontName='Helvetica-Bold'
    )
    
    job_info_style = ParagraphStyle(
        'JobInfo',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#555555'),
        spaceAfter=1,
        fontName='Helvetica-Oblique'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#333333'),
        spaceAfter=1,
        leftIndent=12,
        fontName='Helvetica'
    )
    
    summary_style = ParagraphStyle(
        'Summary',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#333333'),
        spaceAfter=2,
        fontName='Helvetica'
    )
    
    # Add photo if exists
    photo_path = "assets/img/profile/professional_photo.jpg"
    if os.path.exists(photo_path):
        img = Image(photo_path, width=0.8*inch, height=0.8*inch)
        elements.append(img)
        elements.append(Spacer(1, 0.05*inch))
    
    # HEADER - Name and Contact
    elements.append(Paragraph("THATOE NYI", title_style))
    elements.append(Paragraph("Data Analyst | Automation Engineer | Web Developer", subtitle_style))
    elements.append(Paragraph(
        "Bangkok, Thailand | +66 661076077 | thatoebkk@gmail.com | LinkedIn: thatoe-nyi-75a82734b | GitHub: Thatoe98",
        contact_style
    ))
    
    elements.append(Spacer(1, 0.05*inch))
    
    # PROFESSIONAL SUMMARY
    elements.append(Paragraph("PROFESSIONAL SUMMARY", section_heading_style))
    elements.append(HorizontalLine(7*inch, thickness=1))
    elements.append(Spacer(1, 0.02*inch))
    elements.append(Paragraph(
        "Computer Science student with 2+ years of experience in data analysis, workflow automation, and web development. "
        "Proven track record in implementing AI-driven automation solutions using n8n, Python, and modern web frameworks. "
        "Strong analytical skills with expertise in Power BI, SQL, and data visualization.",
        summary_style
    ))
    
    elements.append(Spacer(1, 0.04*inch))
    
    # TECHNICAL SKILLS
    elements.append(Paragraph("TECHNICAL SKILLS", section_heading_style))
    elements.append(HorizontalLine(7*inch, thickness=1))
    elements.append(Spacer(1, 0.02*inch))
    
    skills_text = """
    <b>Data Analysis:</b> Excel, Power BI, Python (pandas, matplotlib, seaborn), SQL (MySQL, PostgreSQL), Data Visualization<br/>
    <b>Programming:</b> Python, JavaScript, TypeScript, HTML/CSS, Next.js, React, Java (OOP), Flutter<br/>
    <b>Automation & AI:</b> n8n, AI Integration, API Development, RAG Systems, LLMs (Gemini, OpenAI)<br/>
    <b>Databases:</b> MySQL, PostgreSQL, Supabase, Database Design (3NF)<br/>
    <b>Tools:</b> Git/GitHub, VS Code, Jupyter Notebooks
    """
    elements.append(Paragraph(skills_text, summary_style))
    
    elements.append(Spacer(1, 0.04*inch))
    
    # PROFESSIONAL EXPERIENCE
    elements.append(Paragraph("PROFESSIONAL EXPERIENCE", section_heading_style))
    elements.append(HorizontalLine(7*inch, thickness=1))
    elements.append(Spacer(1, 0.02*inch))
    
    # Job 1
    elements.append(Paragraph("Co-Founder & Lead Automation Engineer", job_title_style))
    elements.append(Paragraph("Creator AI Tech Co., Ltd. | Bangkok, Thailand | 2024 - Present", job_info_style))
    
    job1_bullets = [
        "Co-founded automation agency delivering AI solutions to local businesses and startups",
        "Engineered custom n8n workflows for expense tracking, email management, and social media, reducing client workload by 80%",
        "Developed Creator AI Tech SaaS solutions including AI video generator and lead generation tools for Myanmar SMEs",
        "Designed and deployed RAG (Retrieval-Augmented Generation) agents to automate customer support interactions"
    ]
    
    for bullet in job1_bullets:
        elements.append(Paragraph(f"• {bullet}", body_style))
    
    elements.append(Spacer(1, 0.03*inch))
    
    # Job 2
    elements.append(Paragraph("Private Tutor (STEM & IGCSE)", job_title_style))
    elements.append(Paragraph("Self-Employed | Yangon, Myanmar & Bangkok, Thailand | 2015 - 2024", job_info_style))
    
    job2_bullets = [
        "Delivered personalized tutoring to diverse students, consistently improving performance",
        "Managed all business aspects maintaining 95%+ client retention"
    ]
    
    for bullet in job2_bullets:
        elements.append(Paragraph(f"• {bullet}", body_style))
    
    elements.append(Spacer(1, 0.04*inch))
    
    # KEY PROJECTS
    elements.append(Paragraph("KEY PROJECTS", section_heading_style))
    elements.append(HorizontalLine(7*inch, thickness=1))
    elements.append(Spacer(1, 0.02*inch))
    
    # Project 1
    elements.append(Paragraph(
        "<b>Blood Inventory Management System</b> | Next.js, TypeScript, Supabase, PostgreSQL",
        job_title_style
    ))
    elements.append(Paragraph(
        "• Full-stack web app connecting hospitals, donors, and patients. 3NF normalized database. GitHub: github.com/Thatoe98/blood_inventory_management",
        body_style
    ))
    
    elements.append(Spacer(1, 0.02*inch))
    
    # Project 2
    elements.append(Paragraph(
        "<b>Restaurant Booking Management System</b> | Next.js, TypeScript, Supabase, n8n",
        job_title_style
    ))
    elements.append(Paragraph(
        "• Scalable reservation platform with customer web app and staff management interface. Real-time PostgreSQL database via Supabase. n8n automation for instant confirmations via email and messaging.",
        body_style
    ))
    
    elements.append(Spacer(1, 0.04*inch))
    
    # EDUCATION
    elements.append(Paragraph("EDUCATION", section_heading_style))
    elements.append(HorizontalLine(7*inch, thickness=1))
    elements.append(Spacer(1, 0.02*inch))
    
    elements.append(Paragraph(
        "<b>Bachelor of Science in Computer Science</b> | GPA: 3.98/4.0 | Expected 2027",
        job_title_style
    ))
    elements.append(Paragraph(
        "Rangsit University, Pathum Thani, Thailand",
        job_info_style
    ))
    
    elements.append(Spacer(1, 0.03*inch))
    
    # CERTIFICATIONS
    elements.append(Paragraph("CERTIFICATIONS", section_heading_style))
    elements.append(HorizontalLine(7*inch, thickness=1))
    elements.append(Spacer(1, 0.02*inch))
    
    certifications = [
        "<b>Meta Data Analyst Professional Certificate</b> - Coursera (2025)",
        "<b>Microsoft Power BI Data Analyst Professional Certificate</b> - Coursera (2025)"
    ]
    
    for cert in certifications:
        elements.append(Paragraph(f"• {cert}", body_style))
    
    # Build PDF
    doc.build(elements)
    
    return filename

if __name__ == "__main__":
    print("Generating ATS-optimized resume...")
    filename = create_resume()
    print(f"✓ Resume generated successfully: {filename}")
    print("\nATS Optimization Features:")
    print("- Standard fonts (Helvetica)")
    print("- Simple layout without tables or graphics")
    print("- Clear section headings")
    print("- Keyword-rich content")
    print("- One-page format")
    print("- Proper spacing and hierarchy")
