import os
import shutil

def purge_demos():
    current_dir = os.getcwd()
    demos_dir = os.path.join(current_dir, "demos")
    
    print("========================================")
    print("🗑️  INITIATING DEMO PIPELINE PURGE")
    print("========================================\n")
    
    if not os.path.exists(demos_dir):
        print("✅ The '/demos' folder does not exist yet. Nothing to clean.")
        return

    # List all items in the /demos folder
    demo_folders = [f for f in os.listdir(demos_dir) if os.path.isdir(os.path.join(demos_dir, f))]
    
    if not demo_folders:
        print("✅ The '/demos' folder is already empty.")
        return
        
    print(f"Found {len(demo_folders)} unpaid demo(s) scheduled for deletion:")
    for folder in demo_folders:
        print(f" ⏳ {folder}")
        
    print("\n⚠️  WARNING: This will permanently delete these demo profiles.")
    print("Live clients in the '/live' folder will NOT be affected.")
    confirm = input("Type 'PURGE' to execute deletion: ")
    
    if confirm == 'PURGE':
        deleted_count = 0
        for folder in demo_folders:
            folder_path = os.path.join(demos_dir, folder)
            try:
                shutil.rmtree(folder_path)
                print(f"💀 NUKED: /demos/{folder}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ ERROR deleting {folder}: {e}")
                
        print("\n========================================")
        print(f"✨ PURGE COMPLETE. {deleted_count} demos erased from the server.")
        print("Terminal Command: git add . && git commit -m \"Routine Demo Purge\" && git push")
        print("========================================")
    else:
        print("Purge aborted. Demos remain active.")

if __name__ == "__main__":
    purge_demos()