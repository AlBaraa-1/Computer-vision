"""
CleanEye - Quick Start Menu
Interactive launcher for all project features
"""

import os
import sys
import subprocess
import socket

def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def print_banner():
    print("\n" + "=" * 70)
    print("🗑️  CleanEye - Smart Garbage Detection System")
    print("    ADIPEC25 Physical Showcase")
    print("=" * 70)

def print_menu():
    print("\n📋 What would you like to do?\n")
    print("  🎯 ADIPEC25 BOOTH DEMOS:")
    print("  [1] 🌐 Launch Network Demo (Mobile + Web - RECOMMENDED)")
    print("  [2] 📱 iVCam Detection (Phone as Webcam)")
    print("  [3] 📸 Test Images (Interactive)")
    print("  [4] 🎬 Test Video Files")
    print()
    print("  🛠️  SETUP & TOOLS:")
    print("  [5] 🔍 Check System Setup")
    print("  [6] 📱 Generate QR Code for Booth")
    print("  [7] 🧹 Clean Up Project")
    print()
    print("  📊 TRAINING & RESULTS:")
    print("  [8] 📊 View Training Results")
    print("  [9] 🔄 Retrain Model")
    print()
    print("  📚 HELP:")
    print("  [h] 📚 Open Documentation")
    print("  [i] ℹ️  File Info & Purposes")
    print("  [q] ❌ Quit")
    print()

def run_command(cmd, description):
    print(f"\n🚀 {description}...")
    print("=" * 70)
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    print("=" * 70)
    input("\nPress Enter to return to menu...")

def open_file(filepath):
    if os.path.exists(filepath):
        if sys.platform == 'win32':
            os.startfile(filepath)
        elif sys.platform == 'darwin':
            subprocess.run(['open', filepath])
        else:
            subprocess.run(['xdg-open', filepath])
    else:
        print(f"❌ File not found: {filepath}")
        input("\nPress Enter to continue...")

def main():
    python_exe = sys.executable
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        print_menu()
        
        choice = input("Select option: ").strip().lower()
        
        if choice == '1':
            # Integrated network demo
            local_ip = get_local_ip()
            
            print("\n🌐 Launching Network Demo (Mobile + Web)")
            print("=" * 70)
            print("📱 Features:")
            print("  ✅ Visitors can use their phone cameras")
            print("  ✅ Upload images from gallery")
            print("  ✅ Access from any device on WiFi")
            print("  ✅ Real-time statistics tracking")
            print()
            print(f"📍 Your IP Address: {local_ip}")
            print(f"\n🔗 Access URLs:")
            print(f"   Local:   http://localhost:8501")
            print(f"   Network: http://{local_ip}:8501")
            print("\n📱 Share with visitors:")
            print(f"   1. Connect to same WiFi")
            print(f"   2. Open: http://{local_ip}:8501")
            print(f"   3. Test garbage detection!")
            print()
            print("💡 TIP: Keep this running during ADIPEC25!")
            print("=" * 70)
            print("🛑 Press Ctrl+C to stop server")
            print("=" * 70)
            print()
            
            try:
                # Start Streamlit with network access
                subprocess.run([
                    "streamlit", "run", "detect_gui.py",
                    "--server.address", "0.0.0.0",
                    "--server.port", "8501",
                    "--server.headless", "true"
                ])
            except KeyboardInterrupt:
                print("\n⚠️  Server stopped by user")
            except Exception as e:
                print(f"\n❌ Error: {e}")
            
            print("=" * 70)
            input("\nPress Enter to return to menu...")
        
        elif choice == '2':
            print("\n🎥 Professional Webcam Detection")
            print("=" * 70)
            print("✨ Features:")
            print("  ✅ iVCam support (use phone as webcam)")
            print("  ✅ Real-time detection logging (JSON + TXT)")
            print("  ✅ Advanced UI overlay")
            print("  ✅ Automatic camera detection")
            print("  ✅ FPS counter and statistics")
            print("\n💡 Setup:")
            print("  1. Install iVCam on phone and PC")
            print("  2. Connect phone to same WiFi as PC")
            print("  3. Start iVCam on both devices")
            print("=" * 70)
            run_command(f'"{python_exe}" detect_pro.py', 
                       "Professional Webcam Detection")
        
        elif choice == '3':
            print("\n📸 Image Detection Test")
            print("=" * 70)
            print("💡 Interactive image tester - choose which image to test!")
            print("=" * 70)
            run_command(f'"{python_exe}" test_images.py', 
                       "Interactive Image Tester")
        
        elif choice == '4':
            print("\n🎬 Video Detection Test")
            print("=" * 70)
            print("💡 Test detection on video files (.mp4, .avi, .mov)")
            print("📁 Place videos in 'media/' folder")
            print("=" * 70)
            run_command(f'"{python_exe}" vid.py', 
                       "Video Detection Tester")
        
        elif choice == '5':
            run_command(f'"{python_exe}" check_setup.py', 
                       "Checking System Setup")
        
        elif choice == '6':
            print("\n📱 QR Code Generator")
            print("=" * 70)
            print("🎯 Purpose: Create QR code for easy visitor access")
            print("📍 Visitors scan → Instant demo access!")
            print("=" * 70)
            
            # Get current IP
            import socket
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ip = s.getsockname()[0]
                s.close()
                print(f"\n📍 Your IP: {ip}")
                print(f"🔗 Demo URL: http://{ip}:8501")
            except:
                print("\n⚠️  Could not detect IP address")
            
            print("\n🎨 Generating QR code...")
            run_command(f'"{python_exe}" generate_qr.py', 
                       "QR Code Generator")
            
            # Open the QR code
            if os.path.exists('cleaneye_qr.png'):
                print("\n✅ QR Code saved: cleaneye_qr.png")
                print("📄 Opening QR code...")
                open_file('cleaneye_qr.png')
        
        elif choice == '7':
            run_command(f'"{python_exe}" cleanup.py', 
                       "Cleaning Up Project")
        
        elif choice == '8':
            run_command(f'"{python_exe}" cleanup.py', 
                       "Cleaning Up Project")
        
        elif choice == '7':
            print("\n📊 Training Results:")
            files_to_open = [
                'runs/detect/garbage_yolo_train8/results.png',
                'runs/detect/garbage_yolo_train8/confusion_matrix.png',
                'training_results.png',
                'confusion_matrix.png'
            ]
            
            opened = False
            for filepath in files_to_open:
                if os.path.exists(filepath):
                    print(f"✅ Opening: {filepath}")
                    open_file(filepath)
                    opened = True
                    break
            
            if not opened:
                print("❌ No training results found")
                print("💡 Train the model first with option [9]")
            
            input("\nPress Enter to continue...")
        
        elif choice == '9':
            print("\n⚠️  WARNING: This will start a new training session")
            print("⏱️  Estimated time: 20-30 minutes")
            confirm = input("\nContinue? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                run_command(f'"{python_exe}" train.py', 
                           "Training Model")
            else:
                print("❌ Training cancelled")
                input("\nPress Enter to continue...")
        
        elif choice == 'h':
            print("\n📚 Opening Documentation...\n")
            docs = [
                ('MOBILE_UPDATE.md', '📱 Mobile Camera Update'),
                ('DEPLOYMENT_GUIDE.md', '🌐 Deployment Guide'),
                ('VISITOR_GUIDE.md', '👥 Visitor Guide'),
                ('PROJECT_COMPLETE.md', '📋 Project Summary'),
                ('README.md', '📖 Main README')
            ]
            
            print("  Available Documentation:")
            for filename, desc in docs:
                if os.path.exists(filename):
                    print(f"  ✅ {desc}: {filename}")
                else:
                    print(f"  ❌ {desc}: Not found")
            
            print("\n💡 Which document to open?")
            print("  [1] Mobile Camera Update (NEW!)")
            print("  [2] Deployment Guide")
            print("  [3] Visitor Guide")
            print("  [4] Project Summary")
            print("  [5] Open all")
            print("  [Enter] Skip")
            
            doc_choice = input("\nSelect: ").strip()
            
            if doc_choice == '1' and os.path.exists('MOBILE_UPDATE.md'):
                open_file('MOBILE_UPDATE.md')
            elif doc_choice == '2' and os.path.exists('DEPLOYMENT_GUIDE.md'):
                open_file('DEPLOYMENT_GUIDE.md')
            elif doc_choice == '3' and os.path.exists('VISITOR_GUIDE.md'):
                open_file('VISITOR_GUIDE.md')
            elif doc_choice == '4' and os.path.exists('PROJECT_COMPLETE.md'):
                open_file('PROJECT_COMPLETE.md')
            elif doc_choice == '5':
                for filename, desc in docs:
                    if os.path.exists(filename):
                        open_file(filename)
            
            input("\nPress Enter to continue...")
        
        elif choice == 'i':
            print("\n" + "=" * 70)
            print("ℹ️  CleanEye - File Purposes & Organization")
            print("=" * 70)
            
            file_info = {
                "🚀 MAIN LAUNCHER": {
                    "start.py": "This menu - All features integrated (including network demo)"
                },
                "🎥 DETECTION SCRIPTS": {
                    "detect_pro.py": "iVCam detection (phone as webcam + logging)",
                    "detect_gui.py": "Streamlit web dashboard (used by network demo)",
                    "detect_gui.py": "Streamlit web dashboard (mobile + web)",
                    "test_images.py": "Interactive image tester (RECOMMENDED)",
                    "GarbageDetector.py": "Simple single image test",
                    "vid.py": "Video file tester with controls"
                },
                "⚙️ SETUP & TRAINING": {
                    "train.py": "Train the YOLO model",
                    "check_setup.py": "Verify system requirements",
                    "cleanup.py": "Remove temporary files",
                    "generate_qr.py": "Create booth QR code"
                },
                "📚 DOCUMENTATION": {
                    "README.md": "Main project overview",
                    "MOBILE_UPDATE.md": "Mobile camera features",
                    "DEPLOYMENT_GUIDE.md": "Network/cloud deployment",
                    "VISITOR_GUIDE.md": "Instructions for booth visitors",
                    "START_MENU_GUIDE.md": "This menu's guide"
                },
                "📁 FOLDERS": {
                    "Weights/": "Trained model weights (best.pt)",
                    "dataset/": "Training images and labels",
                    "media/": "Test images and videos",
                    "outputs/": "Detection logs and screenshots"
                }
            }
            
            for category, files in file_info.items():
                print(f"\n{category}:")
                for filename, description in files.items():
                    print(f"  • {filename:<30} {description}")
            
            print("\n" + "=" * 70)
            print("\n💡 KEY DIFFERENCES:")
            print("  detect_pro.py  → iVCam (phone as webcam with logging)")
            print("  detect_gui.py  → Web interface (mobile camera upload)")
            print("  test_images.py → Interactive image testing (best for images)")
            print("  vid.py         → Video file testing with playback controls")
            print("\n" + "=" * 70)
            input("\nPress Enter to continue...")
        
        elif choice == 'q':
            print("\n👋 Goodbye! Good luck at ADIPEC25! 🚀\n")
            break
        
        else:
            print("\n❌ Invalid option. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        input("\nPress Enter to exit...")
