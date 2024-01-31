import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrackingsocketComponent } from './trackingsocket.component';

describe('TrackingsocketComponent', () => {
  let component: TrackingsocketComponent;
  let fixture: ComponentFixture<TrackingsocketComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TrackingsocketComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TrackingsocketComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
