/*
 *	struct {
 *		bg_res
 *		bg_uncompressed
 *
 *		list<changes>
 *	}
 *
 *	enum ChangeType{
 *		bg,
 *		text,
 *		filter,
 *
 *	}
 *
 *	change {
 *		part_affected: 
 *
 *	}
 *
 *	class Change{
 *		
 *		fn undo(current_image) -> new_image
 *
 *		fn undo(&mut current_image);
 *	}
 *
 *	class BgChange: Change{
 *	
 *
 *	}
 *
 *
 *
 *
 *
 *
 *
 *
 *	every effect we make follows this guideline:
 *		
 *
 *		class SampleEffect{
 *			
 *			function make_change(img);
 *			function undo_change(img);
 *			
 *		}
 *
 *
 *
 *
 *
 *
 *
 *	Architecture/Design for project
 *
 *	obj Canvas{
 *		base_image
 *		linked_list<Change> change_list
 *	}
 *
 *
 * 	[bg_update, filter_app, text, filter]
 *
 *	obj Change{
 *		
 *
 *	}
 *
 *
 * 	FilterChange{
 * 		for p in all_pixels:
 * 			p = change(p)
 * 	}
 * 	UndoFilterChange{
 *
 * */
