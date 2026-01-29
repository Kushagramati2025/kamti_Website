import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import LeadershipMember

def add_leaders():
    leaders = [
        {
            "name": "Dayanand Yardi",
            "position": "Finance and Administration",
            "bio": "As an established finance leader for 30 plus years’, Dayanand has extensive global leadership experience including shareholder value creation, mergers and acquisitions, financial and strategic planning, and budgeting. He has vast experience in managing finance and account functions in corporate as well as public sector companies. In his role at Kushagramti, Dayanand is responsible for the finance function which includes Corporate Finance, Business Finance, Business Planning, Treasury, Taxation, and Investor relations.",
            "image": "leadership/dayanand.png",
            "order": 3
        },
        {
            "name": "Shruthi Malagi",
            "position": "Business Development",
            "bio": "Shruthi Malagi is an astute & result oriented Bid management professional with more than a decade of experience working in a leading IT services company. Her career growth has been in IT & ITES in strategic Business Development, Pre-sales and complex Bid Management across industries and geographies. With strong passion towards business development, she drives company operations, human resources and manages vendor relations.",
            "image": "leadership/shruthi.png",
            "order": 4
        }
    ]

    for leader_data in leaders:
        leader, created = LeadershipMember.objects.get_or_create(
            name=leader_data['name'],
            defaults={
                'position': leader_data['position'],
                'bio': leader_data['bio'],
                'image': leader_data['image'],
                'order': leader_data['order']
            }
        )
        if created:
            print(f"Created leader: {leader.name}")
        else:
            print(f"Leader already exists: {leader.name}")
            # Update fields if needed
            leader.position = leader_data['position']
            leader.bio = leader_data['bio']
            leader.image = leader_data['image'] 
            leader.save()
            print(f"Updated leader: {leader.name}")

if __name__ == '__main__':
    add_leaders()
