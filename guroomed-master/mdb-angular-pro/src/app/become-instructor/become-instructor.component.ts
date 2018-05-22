import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../shared/navbarService/navbar.service';

@Component({
  selector: 'app-become-instructor',
  templateUrl: './become-instructor.component.html',
  styleUrls: ['./become-instructor.component.scss']
})
export class BecomeInstructorComponent implements OnInit {
  public myInterval: number = 0;
  activeSlideIndex: number = 0;

  public itemsList: Object[] = [
    {
      title: 'Choose your topic',
      head1: 'Share your knowledge',
      description1: 'Teach what you know, or teach what you love. You can create a course on almost anything. Millions of students are waiting, eager to learn and we’re here to help you make it happen.',
      head2: 'Teach how you desire',
      description2: 'We have multiple formats you can use to create your course. Teach in the style that makes sense for your topic and personality.'
    },
    {
      title: 'Create a course',
      head1: 'Get started',
      description1: 'Our courses are packed with insights, examples, and opportunities for students to learn by doing and achieve their goals.',
      head2: 'Get support along the way',
      description2: 'Use our resources to create engaging courses using our Teach Hub, a resource center for instructors. Join Studio U, a peer to peer community of instructors, who are also creating their own courses. You’ll see our own team members answering questions and providing insight.'
    },
    {
      title: 'Connect with students',
      head1: 'Start sharing your course',
      description1: 'Once your course is live on our marketplace start sharing it with friends, family, and your followers. Use our marketing guides to help make your course a success. We know you want to share your course with the world, let\'s make sure students can find it.',
      head2: 'Promote to the world',
      description2: 'Students can also find your course through our organic search and our marketing efforts.'
    }
  ]


  constructor(private nav: NavbarService) { }

  ngOnInit() {
    this.nav.show();
  }

  activeSlide(slideNo) {
    this.activeSlideIndex = slideNo;
  }
}
