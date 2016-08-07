**Postmortem**. 
Even a well-documented open-source research code can have unexpected tricks of the trade that only the original authors may know about. 
In the end, we don't know _why_ IBAMR required interior body points to be constrained. 
The published record is incomplete in this regard: we could find no explanation for it in any paper using IBAMR. 
One of the issues may be that our community does not have a habit of communicating negative results, nor of publishing papers about software. 
We learned from this experience that using an open research code and getting correct results with it could involve a long investigative period, potentially requiring communication with the original authors and many failed attempts. 
If the code is not well documented and the original authors not responsive to questions, then building your own code from scratch could be more sensible!
